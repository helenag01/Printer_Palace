import streamlit as st
import pandas as pd
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CPSC408!",
    database = "PrinterPalace"
)

st.markdown("<h1 style='text-align: center;'>Search</h1>", unsafe_allow_html=True)

cursor = db.cursor()
category = st.selectbox(
"Select a category :",
("","Printer Model", "FFF Printer", "SLA Printer", "Resin", "Filament")
)

if (category == "Printer Model"):
    model_name = "%" + st.text_input("Model :") + "%"
    brand_name = "%" + st.text_input("Brand :") + "%" 
    printer_type = "%" + st.text_input("Type :") + "%"
    bed_specs = st.checkbox("Input bed specs")
    if (bed_specs):
        use_range = st.checkbox("Use range for bed specs")
        if (use_range):
            bed_width_range = st.slider(
                "Bed width :",
                0.00, 750.00, (250.00, 500.00)
            )
            bed_length_range = st.slider(
                "Bed length :",
                0.00, 750.00, (250.00, 500.00)
            )
            bed_height_range = st.slider(
                "Bed height :",
                0.00, 1000.00, (250.00, 750.00)
            )
        else:
            bed_width = st.number_input("Bed width :")
            bed_length = st.number_input("Bed length :")
            bed_height = st.number_input("Bed height :")

    options = st.multiselect(
        "What do you want to search for? (Select all that apply) :",
        ("Model", "Brand", "Type", "Bed width", "Bed length", "Bed height")
    )
    fff = st.checkbox("Show FFF printers using printer model filters")
    sla = st.checkbox("Show SLA printers using printer model filters")
    values_list = []
    if (fff):
        values_list.append("fff_printer.printer_name AS Name")
        values_list.append("fff_printer.current_nozzle_type AS Nozzle_Type")
        values_list.append("fff_printer.current_nozzle_size AS Nozzle_Size")
        values_list.append("fff_printer.current_bed_type AS Bed_Type")
    if (sla):
        values_list.append("sla_printer.printer_name AS Name")
    if ("Model" in options):
        values_list.append("printer_model.model_name AS Model")
    if ("Brand" in options):
        values_list.append("brand_name AS Brand")
    if ("Type" in options):
        values_list.append("printer_type AS Type")
    if ("Bed width" in options):
        values_list.append("bed_width AS Bed width")
    if ("Bed length" in options):
        values_list.append("bed_length AS Bed length")
    if ("Bed height" in options):
        values_list.append("bed_height AS Bed height")

    printer_model_button = st.button("Search")
    
    if (printer_model_button):
        if (bed_specs):
            if (use_range):
                if (fff):
                    cursor.execute(
                        """
                        SELECT """ + ", ".join(values_list) +
                        """
                        FROM printer_model
                            INNER JOIN fff_printer USING (model_name)
                        WHERE printer_model.model_name LIKE %s
                            AND brand_name LIKE %s
                            AND printer_type LIKE %s
                            AND bed_width BETWEEN %s AND %s
                            AND bed_length BETWEEN %s AND %s
                            AND bed_height BETWEEN %s AND %s
                        """,
                        (model_name.upper(), brand_name.upper(), printer_type.upper(), 
                        bed_width[0], bed_width[1], bed_length[0],
                        bed_length[1], bed_height[0], bed_height[1])
                    )
                elif (sla):
                    cursor.execute(
                        """
                        SELECT """ + ", ".join(values_list) +
                        """
                        FROM printer_model
                            INNER JOIN sla_printer USING (model_name)
                        WHERE printer_model.model_name LIKE %s
                            AND brand_name LIKE %s
                            AND printer_type LIKE %s
                            AND bed_width BETWEEN %s AND %s
                            AND bed_length BETWEEN %s AND %s
                            AND bed_height BETWEEN %s AND %s
                        """,
                        (model_name.upper(), brand_name.upper(), printer_type.upper(), 
                        bed_width[0], bed_width[1], bed_length[0],
                        bed_length[1], bed_height[0], bed_height[1])
                    )
                cursor.execute(
                        """
                        SELECT """ + ", ".join(values_list) +
                        """
                        FROM printer_model
                        WHERE printer_model.model_name LIKE %s
                            AND brand_name LIKE %s
                            AND printer_type LIKE %s
                            AND bed_width BETWEEN %s AND %s
                            AND bed_length BETWEEN %s AND %s
                            AND bed_height BETWEEN %s AND %s
                        """,
                        (model_name.upper(), brand_name.upper(), printer_type.upper(), 
                        bed_width[0], bed_width[1], bed_length[0],
                        bed_length[1], bed_height[0], bed_height[1])
                    )
            else:
                if (fff):
                    cursor.execute(
                        """
                        SELECT """ + ", ".join(values_list) +
                        """
                        FROM printer_model
                            INNER JOIN fff_printer USING (model_name)
                        WHERE printer_model.model_name LIKE %s
                            AND brand_name LIKE %s
                            AND printer_type LIKE %s
                            AND bed_width = %s
                            AND bed_length = %s
                            AND bed_height = %s
                        """,
                        (model_name.upper(), brand_name.upper(), printer_type.upper(), bed_width, bed_length, bed_height)
                    )
                elif (sla):
                    cursor.execute(
                        """
                        SELECT """ + ", ".join(values_list) +
                        """
                        FROM printer_model
                            INNER JOIN sla_printer USING (model_name)
                        WHERE printer_model.model_name LIKE %s
                            AND brand_name LIKE %s
                            AND printer_type LIKE %s
                            AND bed_width = %s
                            AND bed_length = %s
                            AND bed_height = %s
                        """,
                        (model_name.upper(), brand_name.upper(), printer_type.upper(), bed_width, bed_length, bed_height)
                    )  
                else:
                    cursor.execute(
                        """
                        SELECT """ + ", ".join(values_list) +
                        """
                        FROM printer_model
                        WHERE printer_model.model_name LIKE %s
                            AND brand_name LIKE %s
                            AND printer_type LIKE %s
                            AND bed_width = %s
                            AND bed_length = %s
                            AND bed_height = %s
                        """,
                        (model_name.upper(), brand_name.upper(), printer_type.upper(), bed_width, bed_length, bed_height)
                    )  
        else:
            if (fff):
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM printer_model
                        INNER JOIN fff_printer ON fff_printer.model_name = printer_model.model_name
                    WHERE printer_model.model_name LIKE %s
                        AND brand_name LIKE %s
                        AND printer_type LIKE %s
                    """,
                    (model_name.upper(), brand_name.upper(), printer_type.upper())
                )
            elif (sla):
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM printer_model
                        INNER JOIN sla_printer ON sla_printer.model_name = printer_model.model_name
                    WHERE printer_model.model_name LIKE %s
                        AND brand_name LIKE %s
                        AND printer_type LIKE %s
                    """,
                    (model_name.upper(), brand_name.upper(), printer_type.upper())
                )
            else:
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM printer_model
                    WHERE printer_model.model_name LIKE %s
                        AND brand_name LIKE %s
                        AND printer_type LIKE %s
                    """,
                    (model_name.upper(), brand_name.upper(), printer_type.upper())
                )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
elif (category == "FFF Printer"):
    printer_name = "%" + st.text_input("Name :") + "%"
    model_name = "%" + st.text_input("Model :") + "%"
    current_nozzle_type = "%" + st.text_input("Nozzle type :") + "%"
    current_nozzle_size = st.number_input("Nozzle size :")
    current_bed_type = "%" + st.text_input("Bed type :") + "%"
    filament_specs = st.checkbox("Input filament specs")
    if (filament_specs):
        filament_type = "%" + st.text_input("Type :") + "%"
        brand_name = "%" + st.text_input("Brand :") + "%"
        color = "%" + st.text_input("Color :") + "%"
        quantity_range = st.checkbox("Use range for quantity")
        if (quantity_range):
            filament_quantity_range = st.slider(
                "Quantity :",
                0.00, 100.00, (25.00, 75.00)
            )
        else:
            quantity = st.number_input("Quantity :")
    options = st.multiselect(
        "What do you want to search for? (Select all that apply) :",
        ("Name", "Model", "Nozzle type", "Nozzle size", "Bed type", "Filament type", "Filament brand",
        "Filament color", "Filament quantity")
    )
    values_list = []
    if ("Name" in options):
        values_list.append("fff_printer.printer_name AS Name")
    if ("Model" in options):
        values_list.append("fff_printer.model_name AS Model")
    if ("Nozzle type" in options):
        values_list.append("fff_printer.current_nozzle_type AS Nozzle_Type")
    if ("Nozzle size" in options):
        values_list.append("fff_printer.current_nozzle_size AS Nozzle_Size")
    if ("Bed type" in options):
        values_list.append("fff_printer.current_bed_type AS Bed_Type")
    if ("Filament type" in options):
        values_list.append("filament.filament_type AS Filament_Type")
    if ("Filament brand" in options):
        values_list.append("filament.brand_name AS Filament_Brand")
    if ("Filament color" in options):
        values_list.append("filament.color AS Filament_Color")
    if ("Filament quantity" in options):
        values_list.append("filament.quantity AS Filament_Quantity")

    fff_button = st.button("Search")
    
    if (fff_button):
        if (filament_specs):
            if (quantity_range):
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM fff_printer
                        INNER JOIN filament ON fff_printer.current_filament_id = filament.filament_id
                    WHERE printer_name LIKE %s
                        AND model_name LIKE %s
                        AND current_nozzle_type LIKE %s
                        AND current_nozzle_size = %s
                        AND current_bed_type LIKE %s
                        AND filament_type LIKE %s
                        AND brand_name LIKE %s
                        AND color LIKE %s
                        AND quantity BETWEEN %s AND %s
                    """,
                    (printer_name.upper(), model_name.upper(), current_nozzle_type.upper(),
                    current_nozzle_size, current_bed_type.upper(), filament_type.upper(),
                    brand_name.upper(), color.upper(), filament_quantity_range[0], filament_quantity_range[1])
                )
            else: 
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM fff_printer
                        INNER JOIN filament ON fff_printer.current_filament_id = filament.filament_id
                    WHERE printer_name LIKE %s
                        AND model_name LIKE %s
                        AND current_nozzle_type LIKE %s
                        AND current_nozzle_size = %s
                        AND current_bed_type LIKE %s
                        AND filament_type LIKE %s
                        AND brand_name LIKE %s
                        AND color LIKE %s
                        AND quantity = %s
                    """,
                    (printer_name.upper(), model_name.upper(), current_nozzle_type.upper(),
                    current_nozzle_size, current_bed_type.upper(), filament_type.upper(),
                    brand_name.upper(), color.upper(), quantity)
                )
        else:
            cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM fff_printer
                        INNER JOIN filament ON fff_printer.current_filament_id = filament.filament_id
                    WHERE printer_name LIKE %s
                        AND model_name LIKE %s
                        AND current_nozzle_type LIKE %s
                        AND current_nozzle_size = %s
                        AND current_bed_type LIKE %s
                    """,
                    (printer_name.upper(), model_name.upper(), current_nozzle_type.upper(),
                    current_nozzle_size, current_bed_type.upper())
                )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
elif (category == "SLA Printer"):
    printer_name = st.text_input("Name :")
    model_name = st.text_input("Model :")
    resin_specs = st.checkbox("Input resin specs")
    if (resin_specs):
        brand_name = st.text_input("Brand :")
        color = st.text_input("Color :")
        quantity_range = st.checkbox("Use range for quantity")
        if (quantity_range):
            resin_quantity_range = st.slider(
                "Quantity :",
                0.00, 100.00, (25.00, 75.00)
            )
        else:
            quantity = st.number_input("Quantity :")
    options = st.multiselect(
        "What do you want to search for? (Select all that apply) :",
        ("Name", "Model", "Resin brand", "Resin color", "Resin quantity")
    )
    values_list = []
    if ("Name" in options):
        values_list.append("sla_printer.printer_name AS Name")
    if ("Model" in options):
        values_list.append("sla_printer.model_name AS Model")
    if ("Resin brand" in options):
        values_list.append("resin.brand_name AS Resin_Brand")
    if ("Resin color" in options):
        values_list.append("resin.color AS Resin_Color")
    if ("Resin quantity" in options):
        values_list.append("resin.quantity AS Resin_Quantity")

    sla_button = st.button("Search")
    
    if (sla_button):
        if (resin_specs):
            if (quantity_range):
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM sla_printer
                        INNER JOIN resin ON sla_printer.current_resin_id = resin.resin_id
                    WHERE printer_name LIKE %s
                        AND model_name LIKE %s
                        AND brand_name LIKE %s
                        AND color LIKE %s
                        AND quantity BETWEEN %s AND %s
                    """,
                    (printer_name.upper(), model_name.upper(), brand_name.upper(),
                    color.upper(), resin_quantity_range[0], resin_quantity_range[1])
                )
            else: 
                cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM sla_printer
                        INNER JOIN resin ON sla_printer.current_resin_id = resin.resin_id
                    WHERE printer_name LIKE %s
                        AND model_name LIKE %s
                        AND brand_name LIKE %s
                        AND color LIKE %s
                        AND quantity = %s
                    """,
                    (printer_name.upper(), model_name.upper(),
                    brand_name.upper(), color.upper(), quantity)
                )
        else:
            cursor.execute(
                    """
                    SELECT """ + ", ".join(values_list) +
                    """
                    FROM sla_printer
                        INNER JOIN resin ON sla_printer.current_resin_id = resin.resin_id
                    WHERE printer_name LIKE %s
                        AND model_name LIKE %s
                    """,
                    (printer_name.upper(), model_name.upper())
                )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
elif (category == "Filament"):
    filament_type = "%" + st.text_input("Type :") + "%"
    brand_name = "%" + st.text_input("Brand :") + "%"
    color = "%" + st.text_input("Color :") + "%"
    quantity_range = st.checkbox("Use range for quantity")
    if (quantity_range):
        filament_quantity_range = st.slider(
            "Quantity :",
            0.00, 100.00, (25.00, 75.00)
        )
    else:
        quantity = st.number_input("Quantity :")
    options = st.multiselect(
        "What do you want to search for? (Select all that apply) :",
        ("Filament type", "Filament brand",
        "Filament color", "Filament quantity")
    )
    fff = st.checkbox("Show FFF printers using filtered filaments")
    values_list = []
    if (fff):
        values_list.append("fff_printer.printer_name AS Name")
        values_list.append("fff_printer.model_name AS Model")
        values_list.append("fff_printer.current_nozzle_type AS Nozzle_Type")
        values_list.append("fff_printer.current_nozzle_size AS Nozzle_Size")
        values_list.append("fff_printer.current_bed_type AS Bed_Type")
    if ("Filament type" in options):
        values_list.append("filament.filament_type AS Filament_Type")
    if ("Filament brand" in options):
        values_list.append("filament.brand_name AS Filament_Brand")
    if ("Filament color" in options):
        values_list.append("filament.color AS Filament_Color")
    if ("Filament quantity" in options):
        values_list.append("filament.quantity AS Filament_Quantity")

    filament_button = st.button("Search")
    
    if (filament_button):
        if (quantity_range):
            cursor.execute(
                """
                SELECT """ + ", ".join(values_list) +
                """
                FROM fff_printer
                    INNER JOIN filament ON fff_printer.current_filament_id = filament.filament_id
                WHERE filament_type LIKE %s
                    AND brand_name LIKE %s
                    AND color LIKE %s
                    AND quantity BETWEEN %s AND %s
                """,
                (filament_type.upper(), brand_name.upper(), color.upper(), filament_quantity_range[0], filament_quantity_range[1])
            )
        else: 
            cursor.execute(
                """
                SELECT """ + ", ".join(values_list) +
                """
                FROM fff_printer
                    INNER JOIN filament ON fff_printer.current_filament_id = filament.filament_id
                WHERE filament_type LIKE %s
                    AND brand_name LIKE %s
                    AND color LIKE %s
                    AND quantity = %s
                """,
                (filament_type.upper(), brand_name.upper(), color.upper(), quantity)
            )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
elif (category == "Resin"):
    brand_name = "%" + st.text_input("Brand :") + "%"
    color = "%" + st.text_input("Color :") + "%"
    quantity_range = st.checkbox("Use range for quantity")
    if (quantity_range):
        filament_quantity_range = st.slider(
            "Quantity :",
            0.00, 100.00, (25.00, 75.00)
        )
    else:
        quantity = st.number_input("Quantity :")
    options = st.multiselect(
        "What do you want to search for? (Select all that apply) :",
        ("Resin brand",
        "Resin color", "Resin quantity")
    )
    sla = st.checkbox("Show SLA printers using filtered resins")
    values_list = []
    if (sla):
        values_list.append("sla_printer.printer_name AS Name")
        values_list.append("sla_printer.model_name AS Model")
    if ("Resin brand" in options):
        values_list.append("resin.brand_name AS Resin_Brand")
    if ("Resin color" in options):
        values_list.append("resin.color AS Resin_Color")
    if ("Resin quantity" in options):
        values_list.append("resin.quantity AS Resin_Quantity")

    resin_button = st.button("Search")
    
    if (resin_button):
        if (quantity_range):
            cursor.execute(
                """
                SELECT """ + ", ".join(values_list) +
                """
                FROM sla_printer
                    INNER JOIN resin ON sla_printer.current_resin_id = resin.resin_id
                WHERE brand_name LIKE %s
                    AND color LIKE %s
                    AND quantity BETWEEN %s AND %s
                """,
                (brand_name.upper(), color.upper(), filament_quantity_range[0], filament_quantity_range[1])
            )
        else: 
            cursor.execute(
                """
                SELECT """ + ", ".join(values_list) +
                """
                FROM sla_printer
                    INNER JOIN resin ON sla_printer.current_resin_id = resin.resin_id
                WHERE brand_name LIKE %s
                    AND color LIKE %s
                    AND quantity = %s
                """,
                (brand_name.upper(), color.upper(), quantity)
            )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

