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
    


cursor = db.cursor()
category = st.selectbox(
"Select a category :",
("","Printer Model", "FFF Printer", "SLA Printer", "Resin", "Filament")
)
        
if (category == "Printer Model"):
    model_name = st.text_input("Model :")
    brand_name = st.text_input("Brand :")
    printer_type = st.selectbox(
        "Type :",
        ("", "fff", "sla")
    )
    bed_width = st.number_input("Bed width :")
    bed_length = st.number_input("Bed length :")
    bed_height = st.number_input("Bed height :")
    printer_model_button = st.button("Commit")
elif (category == "FFF Printer"):
    printer_name = st.text_input("Name :")
    cursor.execute(
        """
        SELECT model_name
        FROM printer_model
        WHERE printer_type = "fff"
        """
    )
    models = list(chain(*cursor.fetchall()))
    model_name = st.selectbox(
        "Model :",
        ("", models)
    )
    current_nozzle_type = st.text_input("Nozzle type :")
    current_nozzle_size = st.number_input("Nozzle size :")
    current_bed_type = st.text_input("Bed type :")
    cursor.execute(
        """
        SELECT DISTINCT filament_type
        FROM filament
        """
    )
    filament_types = list(chain(*cursor.fetchall()))
    filament_type = st.selectbox(
        "Filament type :",
        ("", filament_types)
    )
    cursor.execute(
        """
        SELECT DISTINCT brand_name
        FROM filament
        WHERE filament_type = %s
        """,
        (filament_type,)
    )
    filament_brands = list(chain(*cursor.fetchall()))
    filament_brand = st.selectbox(
        "Filament brand :",
        (filament_brands)
    )
    cursor.execute(
        """
        SELECT DISTINCT color
        FROM filament
        WHERE filament_type = %s AND brand_name = %s
        """,
        (filament_type, filament_brand)
    )
    colors = list(chain(*cursor.fetchall()))
    filament_color = st.selectbox(
        "Filament color :",
        ("", colors)
    )
    cursor.execute(
        """
        SELECT filament_id
        FROM filament
        WHERE filament_type = %s AND brand_name = %s AND color = %s
        """,
        (filament_type, filament_brand, filament_color)
    )
    current_filament_id = cursor.fetchone()
    fff_button = st.button("Commit")
elif (category == "SLA Printer"):
    printer_name = st.text_input("Name :")
    model_name = st.text_input("Model :")
    cursor.execute(
        """
        SELECT DISTINCT brand_name
        FROM resin
        """
    )
    resin_names = list(chain(*cursor.fetchall()))
    resin_name = st.selectbox(
        "Resin brand name :",
        ("", resin_names)
    )
    cursor.execute(
        """
        SELECT DISTINCT color
        FROM resin
        WHERE brand_name = %s
        """,
        (resin_name,)
    )
    resin_colors = list(chain(*cursor.fetchall()))
    resin_color = st.selectbox(
        "Resin color :",
        ("", resin_colors)
    )
    cursor.execute(
        """
        SELECT resin_id
        FROM resin
        WHERE brand_name = %s AND color = %s
        """,
        (resin_name.upper(), resin_color.upper())
    )
    current_resin_id = cursor.fetchone()
    sla_button = st.button("Commit")
elif (category == "Resin"):
    brand_name = st.text_input("Brand :")
    color = st.text_input("Color :")
    cursor.execute(
        """
        SELECT 
        FROM resin
        WHERE brand_name = %s AND color = %s
        """,
        (brand_name.upper(), color.upper())
    )
    if (len(cursor.fetchall()) == 0):
        resin_exists = False
    else:
        resin_exists = True
    quantity = st.number_input("Quantity :")
    resin_button = st.button("Commit")
elif (category == "Filament"):
    filament_type = st.text_box("Type :")
    brand_name = st.text_input("Brand :")
    color = st.text_input("Color :")
    cursor.execute(
        """
        SELECT 
        FROM resin
        WHERE brand_name = %s AND color = %s AND type %s
        """,
        (brand_name.upper(), color.upper(), filament_type.upper())
    )
    if (len(cursor.fetchall()) == 0):
        filament_exists = False
    else:
        filament_exists = True
    quantity = st.number_input("Quantity :")
    filament_button = st.button("Commit")





def add_printer_model(printer_model):
    cursor.execute(
        ''' INSERT INTO printer_model VALUES(%s,%s,%s,%s,%s,%s);''', 
        printer_model
    )
    db.commit()

def add_fff_printer(conn, fff_printer):
    cursor.execute(
        ''' INSERT INTO fff_printer(printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, current_filament_id) 
              VALUES(?,?,?,?,?,?) ''', 
        fff_printer
    )
    db.commit()

def add_sla_printer(conn, sla_printer):
    cursor.execute(
        ''' INSERT INTO fff_printer(printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, current_filament_id) 
              VALUES(?,?,?,?,?,?) ''', 
        fff_printer
    )
    db.commit()
    sql = ''' INSERT INTO sla_printer(printer_name, model_name, current_resin_id) 
              VALUES(?,?,?) '''    
    cur = conn.cursor()
    cur.execute(sql, sla_printer)
    conn.commit()

def add_filament(conn, filament):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO filament(filament_type, brand_name, color, quantity)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, filament)
    conn.commit()
