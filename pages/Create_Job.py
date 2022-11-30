import streamlit as st
import mysql.connector
from itertools import chain

st.markdown("<h1 style='text-align: center;'>New Job</h1>", unsafe_allow_html=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "PrinterPalace"
)

def create_job():
    cursor = db.cursor()
    printer_name = st.text_input("Name : ")
    st.write(printer_name)
    cursor.execute("SELECT DISTINCT color FROM filament")
    filament_colors = cursor.fetchall()
    colors = ("blue", "red", "yellow")
    color = st.selectbox(
        "Select a filament color :",
        (filament_colors)
        )
    st.write(color)
    start_time = st.text_input("Start Time :")
    end_time = st.text_input("End Time :")



create_job()