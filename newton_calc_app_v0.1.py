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

st.title('গতিসূত্র ক্যালকুলেটর')

st.write('নিউটনের গতিসূত্র (SUVAT সমীকরণ) দিয়ে সমত্বরণে চলমান বস্তুর গতি হিসাব করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['অজানা চলক নির্বাচন করুন', 'সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'সরণ (s)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)']):
        u = ask_u()
        v = ask_v()
        t = ask_t()
        s = 0.5*(u+v)*t
        st.write('সরণ (s) = ', s)
    elif all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        u = ask_u()
        v = ask_v()
        a = ask_a()
        s = (v*v - u*u)/(2*a)
        st.write('সরণ (s) = ', s)
    elif all(elem in option2  for elem in ['আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)']):
        u = ask_u()
        a = ask_a()
        t = ask_t()
        s = v*t + 0.5*a*t*t
        st.write('সরণ (s) = ', s)
    elif all(elem in option2  for elem in ['শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)']):
        v = ask_v()
        a = ask_a()
        t = ask_t()
        s = v*t - 0.5*a*t*t
        st.write('সরণ (s) = ', s)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের অশূন্য মান আপনার জানা আছে')

elif option == 'আদিবেগ (u)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])
    if all(elem in option2  for elem in ['শেষবেগ (v)', 'ত্বরণ (a)', 'সময় (t)']):
        v = ask_v()
        a = ask_a()
        t = ask_t()
        u = v - (a*t)
        st.write('আদিবেগ (u) = ', u)
    elif all(elem in option2  for elem in ['সরণ (s)', 'ত্বরণ (a)', 'সময় (t)']):
        s = ask_s()
        a = ask_a()
        t = ask_t()
        u = (s - 0.5*a*t*t)/t
        st.write('আদিবেগ (u) = ', u)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'সময় (t)']):
        s = ask_s()
        v = ask_v()
        t = ask_t()
        u = (2*s)/t - v
        st.write('আদিবেগ (u) = ', u)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        s = ask_s()
        v = ask_v()
        a = ask_a()
        u = math.sqrt(v*v - 2*a*s)
        st.write('আদিবেগ (u) = ', u)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের অশূন্য মান আপনার জানা আছে')

elif option == 'শেষবেগ (v)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)','ত্বরণ (a)', 'সময় (t)']):
        u = ask_u()
        a = ask_a()
        t = ask_t()
        v = u + (a*t)
        st.write('শেষবেগ (v) = ', v)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'সময় (t)']):
        s = ask_s()
        u = ask_u()
        t = ask_t()
        v = (2*s)/t - u
        st.write('শেষবেগ (v) = ', v)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)']):
        s = ask_s()
        u = ask_u()
        a = ask_a()
        v = math.sqrt(u*u + 2*a*s)
        st.write('শেষবেগ (v) = ', v)
    elif all(elem in option2  for elem in ['সরণ (s)', 'ত্বরণ (a)', 'সময় (t)']):
        s = ask_s()
        a = ask_a()
        t = ask_t()
        v = (s + 0.5*a*t*t)/t
        st.write('শেষবেগ (v) = ', v)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের অশূন্য মান আপনার জানা আছে')

elif option == 'ত্বরণ (a)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'সময় (t)']):
        u = ask_u()
        v = ask_v()
        t = ask_t()
        a = (v-u)/t
        st.write('ত্বরণ (a) = ', a)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)']):
        s = ask_s()
        u = ask_u()
        v = ask_v()
        a = (v*v - u*u)/(2*s)
        st.write('ত্বরণ (a) = ', a)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'সময় (t)']):
        s = ask_s()
        u = ask_u()
        t = ask_t()
        a = 2*(s-u*t)/(t*t)
        st.write('ত্বরণ (a) = ', a)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'সময় (t)']):
        s = ask_s()
        v = ask_v()
        t = ask_t()
        a = 2*(v*t-s)/(t*t)
        st.write('ত্বরণ (a) = ', a)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের অশূন্য মান আপনার জানা আছে')

elif option == 'সময় (t)':
    option2 = st.multiselect('কোন কোন চলকের মান জানা আছে? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)'])
    if all(elem in option2  for elem in ['আদিবেগ (u)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        u = ask_u()
        v = ask_v()
        a = ask_a()
        t = (v - u) / a
        st.write('সময় (t) = ', t)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'শেষবেগ (v)']):
        s = ask_s()
        u = ask_u()
        v = ask_v()
        t = (2*s)/(u+v)
        st.write('সময় (t) = ', t)
    elif all(elem in option2  for elem in ['সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)']):
        s = ask_s()
        u = ask_u()
        a = ask_a()
        t = -u/a + math.sqrt(u*u +2*a*s)/a
        st.write('সময় (t) = ', t)
    elif all(elem in option2  for elem in ['সরণ (s)', 'শেষবেগ (v)', 'ত্বরণ (a)']):
        s = ask_s()
        v = ask_v()
        a = ask_a()
        t = v/a - math.sqrt(v*v - 2*a*s)/a
        st.write('সময় (t) = ', t)
    else:
        st.write('শুধুমাত্র যেকোন তিনটি চলক নির্বাচন করুন যাদের অশূন্য মান আপনার জানা আছে')
