import mysql.connector

def obtener_conexion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="farmacia_ef"
    )
    return mydb
