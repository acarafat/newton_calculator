import streamlit as st

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

def ask_t():
    u = st.number_input('সময় (t) :')
    return u

############
# Main App #
############
st.title('গতিসূত্র ক্যালকুলেটর')

st.write('s=(1/2)(u+v)t গতিসূত্রের হিসাব বের করতে এই ক্যালকুলেটরটি আপনাকে সাহায্য করবে।')

option = st.selectbox('কোন চলকের মান বের করতে চান? নিচের ড্রপডাউন থেকে নির্ধারণ করুন:', ['চলক সনাক্ত করুন', 'সরণ (s)', 'আদিবেগ (v)', 'ত্বরণ (a)', 'সময় (t)'])

if option == 'সরণ (s)':
    u = ask_u()
    t = ask_t()
    v = ask_v()
    s = 0.5*(u+v)*t
    st.write('s, সরণ = ', s)

elif option == 'আদিবেগ (u)':
    s = ask_s()
    v = ask_v()
    t = ask_t()
    u = (2*s)/t - v
    st.write('u, আদিবেগ = ', u)

elif option == 'শেষবেগ (v)':
    s = ask_s()
    u = ask_u()
    t = ask_t()
    v = (2*s)/t - u
    st.write('v, শেষবেগ = ', v)

elif option == 'সময় (t)':
    u = ask_u()
    v = ask_v()
    s = ask_s()
    t = (2*s)/(u+v)
    st.write('t, সময় = ', t)

else:
    st.write('উপরে কোন চলকের মান গণনা করতে চান সেটা ঠিক করলে বাকি চলকগুলো এখানে নিচে চলে আসবে')
