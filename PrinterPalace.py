import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dukie393!mysql",
    database = "PrinterPalace"
)

# def filament():
#     cursor = db.cursor()
#     cursor.execute(
#         "SELECT * FROM filament INNER JOIN filament_type INNER JOIN filament_brand"
#     )
#     filament_info = cursor.fetchall()
#     return filament_info

# for x in cursor:
#     print(x)