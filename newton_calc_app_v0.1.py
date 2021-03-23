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

st.markdown("<h1 style='text-align: center; color: red; font-family: Solaimanlipi'>গতি-সমীকরণ ক্যালকুলেটর </h1>", unsafe_allow_html=True)

st.write('নিউটনিয়ান গতি-সমীকরণগুলো (SUVAT সমীকরণ) দিয়ে সমত্বরণে চলমান বস্তুর গতীয় চলকগুলো হিসাব করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

st.write('যে চলক তিনটির মান আপনি জানেন, তাদেরকে নির্বাচন করুন:')

option_s = st.checkbox('সরণ (s)')
option_u = st.checkbox('আদিবেগ (u)')
option_v = st.checkbox('শেষবেগ (v)')
option_a = st.checkbox('ত্বরণ (a)')
option_t = st.checkbox('সময় (t)')
known_variables = option_s + option_u + option_v + option_a + option_t

if known_variables <3:
    st.write('কমপক্ষে যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে।')
elif known_variables == 3:
   st.write('আপনার নির্বাচিত ৩টা চলকের মান একই ইউনিট সিস্টেমে লিখুন। সেই অনুযায়ী এই ক্যালকুলেটর বাকি ২টা চলকের মান হিসাব করে জানিয়ে দিবে।')
elif known_variables >3:
    st.write('সর্ব্বোচ্চ যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে।')

if (option_s==False and option_u and option_v and option_a==False and option_t):    # ['আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)']
    u = ask_u()
    v = ask_v()
    t = ask_t()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        s = \\frac{1}{2}(u+v)t, \\quad a = \\frac{v-u}{t}
        $$      """)
        s = 0.5*(u+v)*t
        try:
            a = (v-u)/t
        except ZeroDivisionError:
            st.write('এখানে $t=0$ বসালে চলবে না।')
            a = None
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('সরণ $(s) = \\frac{1}{2}(u+v)t =$ ', s)
        st.write('ত্বরণ $(a) = \\frac{v-u}{t} =$ ', a)

elif (option_s==False and option_u and option_v and option_a and option_t==False):  # ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)']
    u = ask_u()
    v = ask_v()
    a = ask_a()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        s = \\frac{v^2-u^2}{2a}, \\quad t = \\frac{v-u}{a}
        $$      """)
        try:
            s = (v*v - u*u)/(2*a)
            t = (v - u)/a
        except ZeroDivisionError:
            st.write('এখানে $a=0$ বসালে চলবে না।')
            s = None
            t = None
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('সরণ $(s) = \\frac{v^2-u^2}{2a} =$ ', s)
        st.write('সময় $(t) = \\frac{v-u}{a} =$ ', t)

elif (option_s==False and option_u and option_v==False  and option_a and option_t): # ['আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)']
    u = ask_u()
    a = ask_a()
    t = ask_t()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        s = ut + \\frac{1}{2}at^2, \\quad v = u + at
        $$      """)
        s = u*t + 0.5*a*t*t
        v = u + a*t
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('সরণ $(s) = ut + \\frac{1}{2}at^2 =$ ', s)
        st.write('শেষবেগ $(v) = u + at$ ', v)

elif (option_s==False and option_u==False and option_v and option_a and option_t):  # ['শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)']
    v = ask_v()
    a = ask_a()
    t = ask_t()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        s = vt - \\frac{1}{2}at^2, \\quad u= v - at
        $$      """)
        s = v*t - 0.5*a*t*t
        u = v - a*t
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('সরণ $(s) = vt - \\frac{1}{2}at^2 =$ ', s)
        st.write('আদিবেগ $(u) =u - at =$ ', u)

elif (option_s and option_u==False and option_v==False and option_a and option_t):  # ['সরণ (s)', 'ত্বরণ (a)', 'সময় (t)']
    s = ask_s()
    a = ask_a()
    t = ask_t()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        u = \\frac{s}{t} - \\frac{1}{2}at, \\quad v = \\frac{s}{t} + \\frac{1}{2}at
        $$      """)
        try:
            u = (s - 0.5*a*t*t)/t
            v = (s + 0.5*a*t*t)/t
        except ZeroDivisionError:
            st.write('এখানে $t=0$ বসালে চলবে না।')
            u = None
            v = None
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('আদিবেগ $(u) = \\frac{s}{t} - \\frac{1}{2}at =$ ', u)
        st.write('শেষবেগ $(v) = \\frac{s}{t} + \\frac{1}{2}at =$ ', v)

elif (option_s and option_u==False and option_v and option_a==False and option_t):  # ['সরণ (s)', 'শেষবেগ (v)', 'সময় (t)']
    s = ask_s()
    v = ask_v()
    t = ask_t()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        u = \\frac{2s}{t} - v, \\quad a = \\frac{2(vt-s)}{t^2}
        $$      """)
        try:
            u = (2*s)/t - v
            a = 2*(v*t-s)/(t*t)
        except ZeroDivisionError:
            st.write('এখানে $t=0$ বসালে চলবে না।')
            u = None
            a = None
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('আদিবেগ $(u) = \\frac{2s}{t} - v =$ ', u)
        st.write('ত্বরণ $(a)  = \\frac{2(vt-s)}{t^2} =$ ', a)

elif (option_s and option_u==False and option_v and option_a and option_t==False):  # ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)']
    s = ask_s()
    v = ask_v()
    a = ask_a()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        u = \\sqrt{v^2 -2as}, \\quad t = \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a}
        $$      """)
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
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('আদিবেগ $(u) = \\sqrt{v^2 -2as} =$ ', u)
        st.write('সময় $(t)= \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a} =$ ', t)

elif (option_s and option_u and option_v==False and option_a==False and option_t):  # ['সরণ (s)', 'আদিবেগ (u)', 'সময় (t)']
    s = ask_s()
    u = ask_u()
    t = ask_t()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        v = \\frac{2s}{t}-u, \\quad a = \\frac{2(s-ut)}{t^2}
        $$      """)
        try:
            v = (2*s)/t - u
            a = 2*(s-u*t)/(t*t)
        except ZeroDivisionError:
            st.write('এখানে $t=0$ বসালে চলবে না।')
            v = None
            a = None
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('শেষবেগ $(v) = \\frac{2s}{t}-u =$ ', v)
        st.write('ত্বরণ $(a)= \\frac{2(s-ut)}{t^2} =$ ', a)

elif (option_s and option_u and option_v==False and option_a and option_t==False):  # ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)']
    s = ask_s()
    u = ask_u()
    a = ask_a()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        v = \\sqrt{u^2 + 2as}, \\quad t = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a}
        $$      """)
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
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('শেষবেগ $(v) = \\sqrt{u^2 + 2as} =$ ', v)
        st.write('সময় $(t) = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a} =$ ', t)

elif (option_s and option_u and option_v and option_a==False and option_t==False):  # ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)']
    s = ask_s()
    u = ask_u()
    v = ask_v()
    if st.button('বাকি দুই চলকের অজানা মান সমীকরণসহ জানতে এখানে ক্লিক করুন')==True:
        st.write("""        মান নির্ণয়ে ব্যবহৃত সমীকরণদ্বয়:
        $$
        a = \\frac{v^2 - u^2}{2s}, \\quad t = \\frac{2s}{u+v}
        $$      """)
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
        st.write('আপনার দেওয়া মানগুলো উক্ত সমীকরণদ্বয়ে বসিয়ে পাই:')
        st.write('ত্বরণ $(a) = \\frac{v^2 - u^2}{2s} =$ ', a)
        st.write('সময় $(t) = \\frac{2s}{u+v} =$ ', t)
