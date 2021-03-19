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

def ask_v():
    u = st.number_input('শেষবেগ (v) :')
    return u

def ask_a():
    u = st.number_input('ত্বরণ (a) :')
    return u



############
# Main App #
############
st.title('গতিসূত্র ক্যালকুলেটর')

st.write('v^2 = u^2 + 2as গতিসূত্রের হিসাব বের করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['চলক সনাক্ত করুন', 'সরণ (s)', 'আদিবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'সরণ (s)':
    u = ask_u()
    a = ask_a()
    v = ask_v()
    s = (v*v - u*u)/(2*a)
    st.write('s, সরণ = ', s)

elif option == 'আদিবেগ (u)':
    s = ask_s()
    v = ask_v()
    a = ask_a()
    u = math.sqrt(v*v - 2*a*s)
    st.write('u, আদিবেগ = ', u)

elif option == 'শেষবেগ (v)':
    s = ask_s()
    u = ask_u()
    a = ask_a()
    v = math.sqrt(u*u + 2*a*s)
    st.write('v, শেষবেগ = ', v)

elif option == 'ত্বরণ (a)':
    u = ask_u()
    v = ask_v()
    s = ask_s()
    a = (v*v - u*u)/(2*s)
    st.write('a, ত্বরণ = ', a)

else:
    st.write('উপরে কোন চলকের মান গণনা করতে চান সেটা ঠিক করলে বাকি চলকগুলো এখানে নিচে চলে আসবে')
