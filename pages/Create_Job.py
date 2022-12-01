import streamlit as st
import mysql.connector
from itertools import chain

st.markdown("<h1 style='text-align: center;'>New Job</h1>", unsafe_allow_html=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "Printer_Palace"
)

# def create_job():
#     cursor = db.cursor()
#     printer_name = st.text_input("Name : ")
#     st.write(printer_name)
#     cursor.execute("SELECT DISTINCT color FROM filament")
#     filament_colors = cursor.fetchall()
#     colors = list(chain(*filament_colors))
#     color = st.selectbox(
#         "Select a filament color :",
#         (colors)
#         )
#     cursor.execute("SELECT DISTINCT filament_name FROM filament_type INNER JOIN filament WHERE color = color")
#     filament_types = cursor.fetchall()
#     types = list(chain(*filament_types))
#     type = st.selectbox(
#         "Select a filament type :",
#         (types)
#     )
#     start_time = st.text_input("Start Date/Time (use YYYY-MM-DD hh:mm:ss):")
#     end_time = st.text_input("End Date/Time (use YYYY-MM-DD hh:mm:ss):")



# create_job()