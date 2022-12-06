import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "PrinterPalace"
)

st.markdown("<h1 style='text-align: center;'>Update</h1>", unsafe_allow_html=True)

# STREAMLIT

# update all fields everytime there is any update by using old values for simplification

cursor = db.cursor()

category = st.selectbox(
"Select a category :",
("","Printer Model", "FFF Printer", "Nozzle Swap", "SLA Printer", "Resin", "Filament")
)

if (category != "Nozzle Swap"):
    cursor.execute('''COMMIT;''')
if (category == "Nozzle Swap"):
    cursor.execute(
        """
        SELECT printer_name FROM fff_printer
        ORDER BY printer_name;
        """
    )
    printers = cursor.fetchall()
    printers = list(chain(*printers))
    cursor.execute(
        """
        SELECT current_nozzle_type FROM fff_printer
        ORDER BY printer_name;
        """
    )
    nozzles = cursor.fetchall()
    nozzles = list(chain(*nozzles))

    printers = [""] + printers
    printer_1 = st.selectbox(
        "Printer 1 :",
        (printers))
    if printer_1 != "":
        p1idx = printers.index(printer_1)
        # st.text(nozzles[p1idx])

        printers_mod = printers
        nozzles_mod = nozzles

        # del printers_mod[p1idx]
        # del nozzles_mod[p1idx]

        printer_2 = st.selectbox(
        "Printer 2 :",
        (printers_mod))

        if printer_2 == printer_1:
            st.error("ERROR - Select 2 different printers")
        elif printer_2 != "":
            # with st.container():
            #     st.text(nozzles_mod[p1idx])
            button = st.button("Swap")
            if button:
                cursor.execute(
                    '''START TRANSACTION;'''
                )
                cursor.execute(
                    '''CALL sp_getNozzle(%s, @t);''',(printer_1,)
                )
                cursor.execute(
                    '''CALL sp_getNozzle(%s, @u);''',(printer_2,)
                )
                cursor.execute(
                    '''SAVEPOINT x;'''
                )
                cursor.execute(
                    '''UPDATE fff_printer
                        SET current_nozzle_type = @t
                        WHERE printer_name = %s;''', (printer_2,)
                )
                cursor.execute(
                    '''UPDATE fff_printer
                        SET current_nozzle_type = @u
                        WHERE printer_name = %s;''', (printer_1,)
                )
                undo = st.button("Undo")
                if undo:
                    cursor.execute(
                    '''ROLLBACK TO x;'''
                    )
        else:
            cursor.execute('''COMMIT;''')
    else:
        cursor.execute('''COMMIT;''')