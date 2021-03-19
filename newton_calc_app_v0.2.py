import streamlit as st
import math

#############
# Variables #
#############
def ask_s():
    s = st.number_input('সরণ (s) :')
    return s

def ask_u():
    u = st.number_input('আদিবেগ (u) :')
    return u

def ask_v():
    v = st.number_input('শেষবেগ (v) :')
    return v

def ask_a():
    a = st.number_input('ত্বরণ (a) :')
    return a

def ask_t():
    t = st.number_input('সময় (t) :')
    return t

############
# Main App #
############

st.title('গতি-সমীকরণ ক্যালকুলেটর')

st.write('নিউটনিয়ান গতি-সমীকরণগুলো (SUVAT সমীকরণ) দিয়ে সমত্বরণে চলমান বস্তুর গতি হিসাব করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['অজানা চলক নির্বাচন করুন', 'সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'সরণ (s)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)']):
        u = ask_u()
        v = ask_v()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $s = \\frac{1}{2}(u+v)t$')
        s = 0.5*(u+v)*t
        st.write('সরণ (s) = ', s)
    elif all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        u = ask_u()
        v = ask_v()
        a = ask_a()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $s = \\frac{v^2-u^2}{2a}$')
        s = (v*v - u*u)/(2*a)
        st.write('সরণ (s) = ', s)
    elif all(elem in option2  for elem in ['আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)']):
        u = ask_u()
        a = ask_a()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $s = ut + \\frac{1}{2}at^2$')
        s = u*t + 0.5*a*t*t
        st.write('সরণ (s) = ', s)
    elif all(elem in option2  for elem in ['শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)']):
        v = ask_v()
        a = ask_a()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $s = vt - \\frac{1}{2}at^2$')
        s = v*t - 0.5*a*t*t
        st.write('সরণ (s) = ', s)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে')

elif option == 'আদিবেগ (u)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])
    if all(elem in option2  for elem in ['শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)']):
        v = ask_v()
        a = ask_a()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $u = v -at$')
        u = v - (a*t)
        st.write('আদিবেগ (u) = ', u)
    elif all(elem in option2  for elem in ['সরণ (s)', 'ত্বরণ (a)', 'সময় (t)']):
        s = ask_s()
        a = ask_a()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $u = \\frac{s}{t} \\frac{1}{2}at$')
        u = (s - 0.5*a*t*t)/t
        st.write('আদিবেগ (u) = ', u)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'সময় (t)']):
        s = ask_s()
        v = ask_v()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $u = \\frac{2s}{t} - v$')
        u = (2*s)/t - v
        st.write('আদিবেগ (u) = ', u)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        s = ask_s()
        v = ask_v()
        a = ask_a()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $u = \\sqrt{v^2 -2as}$')
        u = math.sqrt(v*v - 2*a*s)
        st.write('আদিবেগ (u) = ', u)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে')

elif option == 'শেষবেগ (v)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)','ত্বরণ (a)', 'সময় (t)']):
        u = ask_u()
        a = ask_a()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $v = u + at$')
        v = u + (a*t)
        st.write('শেষবেগ (v) = ', v)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'সময় (t)']):
        s = ask_s()
        u = ask_u()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $v = \\frac{2s}{t} -u$')
        v = (2*s)/t - u
        st.write('শেষবেগ (v) = ', v)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)']):
        s = ask_s()
        u = ask_u()
        a = ask_a()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $v = \\sqrt{u^2 + 2as}$')
        v = math.sqrt(u*u + 2*a*s)
        st.write('শেষবেগ (v) = ', v)
    elif all(elem in option2  for elem in ['সরণ (s)', 'ত্বরণ (a)', 'সময় (t)']):
        s = ask_s()
        a = ask_a()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $v = \\frac{s}{t} + \\frac{1}{2}at$')
        v = (s + 0.5*a*t*t)/t
        st.write('শেষবেগ (v) = ', v)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে')

elif option == 'ত্বরণ (a)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)']):
        u = ask_u()
        v = ask_v()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $a = \\frac{v-u}{t}$')
        a = (v-u)/t
        st.write('ত্বরণ (a) = ', a)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)']):
        s = ask_s()
        u = ask_u()
        v = ask_v()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $a = \\frac{v^2 - u^2}{2s}$')
        a = (v*v - u*u)/(2*s)
        st.write('ত্বরণ (a) = ', a)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'সময় (t)']):
        s = ask_s()
        u = ask_u()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $a = \\frac{2(s-ut)}{t^2}$')
        a = 2*(s-u*t)/(t*t)
        st.write('ত্বরণ (a) = ', a)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'সময় (t)']):
        s = ask_s()
        v = ask_v()
        t = ask_t()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $a = \\frac{2(vt-s)}{t^2}$')
        a = 2*(v*t-s)/(t*t)
        st.write('ত্বরণ (a) = ', a)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে')

elif option == 'সময় (t)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        u = ask_u()
        v = ask_v()
        a = ask_a()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $t = \\frac{v-u}{a}$')
        t = (v - u) / a
        st.write('সময় (t) = ', t)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)']):
        s = ask_s()
        u = ask_u()
        v = ask_v()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $t = \\frac{2s}{u+v}$')
        t = (2*s)/(u+v)
        st.write('সময় (t) = ', t)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)']):
        s = ask_s()
        u = ask_u()
        a = ask_a()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে: $t = -\\frac{u}{a} + \\frac{\\sqrt{u^2 + 2as}}{a}$')
        t = -u/a + math.sqrt(u*u +2*a*s)/a
        st.write('সময় (t) = ', t)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        s = ask_s()
        v = ask_v()
        a = ask_a()
        st.write('যে সমীকরণ ব্যবহার করে ফলাফল দেওয়া হচ্ছে:  $t = \\frac{v}{a} - \\frac{\\sqrt{v^2 - 2as}}{a}$')
        t = v/a - math.sqrt(v*v - 2*a*s)/a
        st.write('সময় (t) = ', t)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের মান আপনার জানা আছে')
