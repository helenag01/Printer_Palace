import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "Printer_Palace"
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
    
    if (table_selection == "Printer"):
        printer_name = st.text_input("Printer name :")
        cursor.execute(
            """
            SELECT DISTINCT brand_name
            FROM printer_brand
            """
        )
        brands = cursor.fetchall()
        printer_brands = list(chain(*brands))
        brand_selection = st.selectbox(
            "Select a printer brand",
            (printer_brands)
        )





create_record()