import streamlit as st

st.write("HELLO WORLD")

option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))

search = st.text_input("Query")

st.write('You searched:', search)

st.write('You selected:', option)