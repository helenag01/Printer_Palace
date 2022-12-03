import mysql.connector
import pandas as pd
from io import StringIO
import numpy as np
import streamlit as st
from itertools import chain


# db = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "CPSC408!",
#         database = "sakila"
#     )

# cursor = db.cursor()
# cursor.execute(
#     """
#     SELECT first_name
#     FROM actor
#     """
# )

# nameData = cursor.fetchall()

# names = list(chain(*nameData))


# st.selectbox(
#     "select",
#     (names)
# )

# def search():
#     st.markdown("<h1 style='text-align: center;'>Search</h1>", unsafe_allow_html=True)
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         SELECT *
#         FROM actor
#         """
#     )

#     columns = [column[0] for column in cursor.description]
#     data = cursor.fetchall()

#     df = pd.DataFrame(data, columns=columns)

#     st.write(df.to_markdown(index=False))

    
# def update():
#     st.markdown("<h1 style='text-align: center;'>Update</h1>", unsafe_allow_html=True)
#     with st.form("my_form"):
#         st.write("Inside the form")
#         slider_val = st.slider("Form slider")
#         checkbox_val = st.checkbox("Form checkbox")

#     # Every form must have a submit button.
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             st.write("slider", slider_val, "checkbox", checkbox_val)

#     st.write("Outside the form")

# def delete():
#     st.markdown("<h1 style='text-align: center;'>Delete</h1>", unsafe_allow_html=True)

# def create():
#     st.markdown("<h1 style='text-align: center;'>Create</h1>", unsafe_allow_html=True)

# search_button = st.sidebar.button("Search", on_click = search)
# update_button = st.sidebar.button("Update", on_click = update)
# delete_button = st.sidebar.button("Delete", on_click = delete)
# create_button = st.sidebar.button("Create", on_click = update)


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "sakila"
)

cursor = db.cursor()
cursor.execute(
    """
    SELECT *
    FROM actor
    """
)

columns = [column[0] for column in cursor.description]
data = cursor.fetchall()

df = pd.DataFrame(data, columns=columns)

st.write(df)

