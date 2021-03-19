import streamlit as st
import math

#############
# Variables #
#############
def ask_s():
    u = st.number_input('সরণ (s) :')
    return u

def ask_v():
    u = st.number_input('শেষবেগ (v) :')
    return u

def ask_a():
    u = st.number_input('ত্বরণ (a) :')
    return u

def ask_t():
    u = st.number_input('সময় (t) :')
    return u



############
# Main App #
############
st.title('গতিসূত্র ক্যালকুলেটর')

st.write('s=vt-(1/2)at^2 গতিসূত্রের হিসাব বের করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['চলক সনাক্ত করুন', 'সরণ (s)', 'আদিবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'সরণ (s)':
    a = ask_a()
    t = ask_t()
    v = ask_v()
    s = v*t - 0.5*a*t*t
    st.write('s, সরণ = ', s)

elif option == 'শেষবেগ (v)':
    s = ask_s()
    a = ask_a()
    t = ask_t()
    v = (s + 0.5*a*t*t)/t
    st.write('v, শেষবেগ = ', v)

elif option == 'ত্বরণ (a)':
    s = ask_s()
    v = ask_v()
    t = ask_t()
    a = 2*(v*t-s)/(t*t)
    st.write('a, ত্বরণ = ', a)

elif option == 'সময় (t)':
    a = ask_a()
    v = ask_v()
    s = ask_s()
    t = v/a - math.sqrt(v*v - 2*a*s)/a
    st.write('t, সময় = ', t)

else:
    st.write('উপরে কোন চলকের মান গণনা করতে চান সেটা ঠিক করলে বাকি চলকগুলো এখানে নিচে চলে আসবে')
