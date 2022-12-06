import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "PrinterPalace"
)

st.markdown("<h1 style='text-align: center;'>Delete</h1>", unsafe_allow_html=True)




    

