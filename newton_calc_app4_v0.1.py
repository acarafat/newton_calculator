import streamlit as st
import math

#############
# Variables #
#############
def ask_s():
    u = st.number_input('সরণ (s) :')
    return u

def ask_u():
    u = st.number_input('আদিবেগ (u) :')
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

st.write('s=ut+(1/2)at^2 গতিসূত্রের হিসাব বের করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['চলক সনাক্ত করুন', 'সরণ (s)', 'আদিবেগ (u)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'সরণ (s)':
    a = ask_a()
    t = ask_t()
    u = ask_u()
    s = v*t + 0.5*a*t*t
    st.write('s, সরণ = ', s)

elif option == 'আদিবেগ (u)':
    s = ask_s()
    a = ask_a()
    t = ask_t()
    u = (s - 0.5*a*t*t)/t
    st.write('u, আদিবেগ = ', u)

elif option == 'ত্বরণ (a)':
    s = ask_s()
    u = ask_u()
    t = ask_t()
    a = 2*(s-u*t)/(t*t)
    st.write('a, ত্বরণ = ', a)

elif option == 'সময় (t)':
    a = ask_a()
    u = ask_u()
    v = ask_v()
    t = -u/a + math.sqrt(u*u +2*a*s)/a
    st.write('t, সময় = ', t)

else:
    st.write('উপরে কোন চলকের মান গণনা করতে চান সেটা ঠিক করলে বাকি চলকগুলো এখানে নিচে চলে আসবে')
