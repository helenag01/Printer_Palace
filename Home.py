import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "PrinterPalace"
)

cursor = db.cursor()

cursor.execute(
    """
    SELECT *
    FROM filament
    WHERE filament_type = "PLA" AND brand_name = "Prusament"
    """
)

st.write(cursor.fetchall())


col1, col2, col3 = st.columns([1,4.5,1])


st.balloons()

with col2:
    st.markdown("<h1 style='text-align: center;'>~ Printer Palace ~</h1>", unsafe_allow_html=True)
    st.markdown("![Alt Text](https://media.giphy.com/media/h5LYyNFkOk0MjIArZW/giphy.gif)")


