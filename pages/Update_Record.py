import streamlit as st
import pandas as pd
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dukie393!mysql",
    database = "PrinterPalace"
)

st.markdown("<h1 style='text-align: center;'>Update</h1>", unsafe_allow_html=True)

# STREAMLIT

# update all fields everytime there is any update by using old values for simplification

cursor = db.cursor()

def update_printer_model(values_to_update):
    cursor.execute(
        """
        SELECT * FROM printer_model
        WHERE printer_model.model_name LIKE %s
        AND brand_name LIKE %s
        AND printer_type LIKE %s
        AND bed_width BETWEEN %s AND %s
        AND bed_length BETWEEN %s AND %s
        AND bed_height BETWEEN %s AND %s;
        """, values_to_update
    )
    columns = [column[0] for column in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    st.write(df)

    mod_value = st.selectbox(
        "Value to modify:",
        ("", "Model", "Brand", "Type", "Bed width", "Bed length", "Bed height")
    )
    
    if mod_value == "Model":
        mod = "printer_model"
        new_value = st.text_input("New Model :")
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model
            SET %s = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (mod, new_value) + values_to_update)
    elif mod_value == "Brand":
        mod = "brand_name"
        new_value = st.text_input("New Brand :")
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model
            SET %s = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (mod, new_value) + values_to_update)

    elif mod_value == "Type":
        mod = "printer_type"
        new_value = st.selectbox(
            "New Type :",
            ("", "FFF", "SLA")
        )
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model
            SET %s = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (mod, new_value) + values_to_update)

    elif mod_value == "Bed width":
        mod = "bed_width"
        new_value = str(st.number_input("New Bed width :"))
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model
            SET %s = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (mod, new_value) + values_to_update)

    elif mod_value == "Bed length":
        mod = "bed_length"
        new_value = str(st.number_input("New Bed length :"))       
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model
            SET %s = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (mod, new_value) + values_to_update)

    elif mod_value == "Bed height":
        mod = "bed_height"
        new_value = str(st.number_input("New Bed height :"))
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model
            SET %s = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (mod, new_value) + values_to_update)

category = st.selectbox(
"Select record type:",
("","Printer Model", "FFF Printer", "Nozzle Swap", "SLA Printer", "Resin", "Filament")
)

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
                    '''
                    START TRANSACTION;
                    CALL sp_getNozzle(%s, @t);
                    CALL sp_getNozzle(%s, @u);
                    SAVEPOINT x;
                    UPDATE fff_printer
                        SET current_nozzle_type = @t
                        WHERE printer_name = %s;
                    UPDATE fff_printer
                        SET current_nozzle_type = @u
                        WHERE printer_name = %s;
                    COMMIT;
                    '''
                    ,(printer_1, printer_2, printer_2, printer_1)
                )

elif "Printer Model":
    model_name = st.text_input("Model :")
    brand_name = st.text_input("Brand :")
    printer_type = st.selectbox(
        "Type :",
        ("", "FFF", "SLA")
    )
    bed_width = st.number_input("Bed width :")
    bed_length = st.number_input("Bed length :")
    bed_height = st.number_input("Bed height :")
    printer_model_button = st.button("Show Entries to be Updated")
    if printer_model_button:
        if bed_height == 0:
            bh_low = "0"
            bh_high = "9999999"
        else:
            bh_low = str(bed_height)
            bh_high = str(bed_height)


        if bed_width == 0:
            bw_low = "0"
            bw_high = "9999999"
        else:
            bw_low = str(bed_width)
            bw_high = str(bed_width)


        if bed_length == 0:
            bl_low = "0"
            bl_high = "9999999"
        else:
            bl_low = str(bed_length)
            bl_high = str(bed_length)


        printer_model = ("%"+model_name.upper()+"%", "%"+brand_name.upper()+"%", "%"+printer_type.upper()+"%", bw_low, bw_high, bl_low, bl_high, bh_low, bh_high)
        update_printer_model(printer_model)

elif "FFF Printer":
    pass

elif "Nozzle Swap":
    pass

elif "SLA Printer":
    pass

elif "Resin":
    pass

elif "Filament":
    pass