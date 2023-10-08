import streamlit as st
st.title('hello,world')

name=st.text_input('Name')

but=st.button('submit')

if but:
    st.write(f'hi,{name} welcome to the session')