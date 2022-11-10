# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def search():
    st.markdown("<h1 style='text-align: center;'>Search</h1>", unsafe_allow_html=True)

def update():
    st.markdown("<h1 style='text-align: center;'>Update</h1>", unsafe_allow_html=True)

def delete():
    st.markdown("<h1 style='text-align: center;'>Delete</h1>", unsafe_allow_html=True)

def create():
    st.markdown("<h1 style='text-align: center;'>Create</h1>", unsafe_allow_html=True)

search_button = st.sidebar.button("Search", on_click = search)
update_button = st.sidebar.button("Update", on_click = update)
delete_button = st.sidebar.button("Delete", on_click = delete)
create_button = st.sidebar.button("Create", on_click = update)

# import streamlit as st

# button = st.button("Search")
# butto = st.button("Create")
# butt = st.button("Delete")
# but = st.button("Update")

# st.write("HELLO WORLD")

# option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))

# search = st.text_input("Query")

# st.write('You searched:', search)

# st.write('You selected:', option)

# st.write('You selected:', button)

# def main_page():
#     if button:
#         st.session_state.runpage=search_page
#         st.experimental_rerun()

# def search_page():
#     st.write('WORKED')