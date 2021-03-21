import streamlit as st
import math

#############
# Variables #
#############
def ask_s():
    s = st.number_input('সরণ (s) :', step=None, format='%f')
    return s

def ask_u():
    u = st.number_input('আদিবেগ (u) :', step=None, format='%f')
    return u

def ask_v():
    v = st.number_input('শেষবেগ (v) :', step=None, format='%f')
    return v

def ask_a():
    a = st.number_input('ত্বরণ (a) :', step=None, format='%f')
    return a

def ask_t():
    t = st.number_input('সময় (t) :', step=None, format='%f')
    return t

############
# Main App #
############
st.title('গতি-সমীকরণ ক্যালকুলেটর')

st.write('নিউটনিয়ান গতি-সমীকরণগুলো (SUVAT সমীকরণ) দিয়ে সমত্বরণে চলমান বস্তুর গতি হিসাব করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

known_variables = st.multiselect('যে চলক তিনটির মান আপনি জানেন, তাদেরকে এই ড্রপডাউন থেকে নির্বাচন করুন এবং একই ইউনিট সিস্টেমে মানগুলো লিখুন:', ['সরণ (s)','আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

while len(known_variables)>3:
    del known_variables[-2]

if all(elem in known_variables  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)']):
    u = ask_u()
    v = ask_v()
    t = ask_t()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $s = \\frac{1}{2}(u+v)t, \\, a = \\frac{v-u}{t}$')
    s = 0.5*(u+v)*t
    try:
        a = (v-u)/t
    except ZeroDivisionError:
        st.write('এখানে $t=0$ বসালে চলবে না।')
        a = None
    st.write('সরণ $(s) = \\frac{1}{2}(u+v)t =$ ', s)
    st.write('ত্বরণ $(a) = \\frac{v-u}{t} =$ ', a)

elif all(elem in known_variables  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
    u = ask_u()
    v = ask_v()
    a = ask_a()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $s = \\frac{v^2-u^2}{2a}, \\, t = \\frac{v-u}{a}$')
    try:
        s = (v*v - u*u)/(2*a)
        t = (v - u)/a
    except ZeroDivisionError:
        st.write('এখানে $a=0$ বসালে চলবে না।')
        s = None
        t = None
    st.write('সরণ $(s) = \\frac{v^2-u^2}{2a} =$ ', s)
    st.write('সময় $(t) = \\frac{v-u}{a} =$ ', t)

elif all(elem in known_variables  for elem in ['আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)']):
    u = ask_u()
    a = ask_a()
    t = ask_t()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $s = ut + \\frac{1}{2}at^2, \\, v = u + at$')
    s = u*t + 0.5*a*t*t
    v = u + a*t
    st.write('সরণ $(s) = ut + \\frac{1}{2}at^2 =$ ', s)
    st.write('শেষবেগ $(v) = u + at$ ', v)

elif all(elem in known_variables  for elem in ['শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)']):
    v = ask_v()
    a = ask_a()
    t = ask_t()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $s = vt - \\frac{1}{2}at^2, \\, u= v - at$')
    s = v*t - 0.5*a*t*t
    u = v - a*t
    st.write('সরণ $(s) = vt - \\frac{1}{2}at^2 =$ ', s)
    st.write('আদিবেগ $(u) =u - at =$ ', u)

elif all(elem in known_variables  for elem in ['সরণ (s)', 'ত্বরণ (a)', 'সময় (t)']):
    s = ask_s()
    a = ask_a()
    t = ask_t()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $u = \\frac{s}{t} \\frac{1}{2}at, \\, v = \\frac{s}{t} + \\frac{1}{2}at $')
    try:
        u = (s - 0.5*a*t*t)/t
        v = (s + 0.5*a*t*t)/t
    except ZeroDivisionError:
        st.write('এখানে $t=0$ বসালে চলবে না।')
        u = None
        v = None
    st.write('আদিবেগ $(u) = \\frac{s}{t} \\frac{1}{2}at =$ ', u)
    st.write('শেষবেগ $(v) = \\frac{s}{t} + \\frac{1}{2}at =$ ', v)

elif all(elem in known_variables  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'সময় (t)']):
    s = ask_s()
    v = ask_v()
    t = ask_t()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $u = \\frac{2s}{t} - v, \\, a = \\frac{2(vt-s)}{t^2}$')
    try:
        u = (2*s)/t - v
        a = 2*(v*t-s)/(t*t)
    except ZeroDivisionError:
        st.write('এখানে $t=0$ বসালে চলবে না।')
        u = None
        a = None
    st.write('আদিবেগ $(u) = \\frac{2s}{t} - v =$ ', u)
    st.write('ত্বরণ $(a)  = \\frac{2(vt-s)}{t^2} =$ ', a)

elif all(elem in known_variables  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
    s = ask_s()
    v = ask_v()
    a = ask_a()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $u = \\sqrt{v^2 -2as}, \\, t = \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a}$')
    try:
        u = math.sqrt(v*v - 2*a*s)
        t = v/a - math.sqrt(v*v - 2*a*s)/a
    except ZeroDivisionError:
        st.write('এখানে $a=0$ বসালে চলবে না।')
        t = None
    except ValueError:
        st.write('এখানে $v^2 < 2as$ বসালে চলবে না।')
        u = None
        t = None
    st.write('আদিবেগ $(u) = \\sqrt{v^2 -2as} =$ ', u)
    st.write('সময় $(t)= \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a} =$ ', t)

elif all(elem in known_variables  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'সময় (t)']):
    s = ask_s()
    u = ask_u()
    t = ask_t()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $v = \\frac{2s}{t}-u, \\, a = \\frac{2(s-ut)}{t^2}$')
    try:
        v = (2*s)/t - u
        a = 2*(s-u*t)/(t*t)
    except ZeroDivisionError:
        st.write('এখানে $t=0$ বসালে চলবে না।')
        v = None
        a = None
    st.write('শেষবেগ $(v) = \\frac{2s}{t}-u =$ ', v)
    st.write('ত্বরণ $(a)= \\frac{2(s-ut)}{t^2} =$ ', a)

elif all(elem in known_variables  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)']):
    s = ask_s()
    u = ask_u()
    a = ask_a()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $v = \\sqrt{u^2 + 2as}, \\, t = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a}$')
    try:
        v = math.sqrt(u*u + 2*a*s)
        t = -u/a + math.sqrt(u*u +2*a*s)/a
    except ZeroDivisionError:
        st.write('এখানে $a=0$ বসালে চলবে না।')
        t = None
    except ValueError:
        st.write('এখানে $v^2 < 2as$ বসালে চলবে না।')
        v = None
        t = None
    st.write('শেষবেগ $(v) = \\sqrt{u^2 + 2as} =$ ', v)
    st.write('সময় $(t) = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a} =$ ', t)

elif all(elem in known_variables  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)']):
    s = ask_s()
    u = ask_u()
    v = ask_v()
    st.write('অজানা চলক দুইটির মান নির্ণয়ে ব্যবহৃত সমীকরণ: $a = \\frac{v^2 - u^2}{2s}, \\, t = \\frac{2s}{u+v}$')
    try:
        a = (v*v - u*u)/(2*s)
    except ZeroDivisionError:
        st.write('এখানে $s=0$ বসালে চলবে না।')
        a = None
    try:
        t = (2*s)/(u+v)
    except ZeroDivisionError:
        st.write('এখানে $u=v=0$ বসালে চলবে না।')
        t = None
    st.write('ত্বরণ $(a) = \\frac{v^2 - u^2}{2s} =$ ', a)
    st.write('সময় $(t) = \\frac{2s}{u+v} =$ ', t)

else:
    st.write('কমপক্ষে যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে।')
