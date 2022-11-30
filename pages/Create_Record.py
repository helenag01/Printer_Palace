import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "PrinterPalace"
)

st.markdown("<h1 style='text-align: center;'>New Record</h1>", unsafe_allow_html=True)

# back = st.button("Back")

# submit = st.button("Submit")
    

def create_record():
    cursor = db.cursor()
    category = st.selectbox(
        "Select a category :",
        ("Printer", "Filament")
        )
        
    if (category == "Printer"):
        table_selection = st.selectbox(
        "Create a new...",
        ("Printer", "Printer brand", "Printer model")
        )
    else:
        table_selection = st.selectbox(
        "Create a new...",
        ("Filament", "Filament brand", "Filament type")
        )

create_record()