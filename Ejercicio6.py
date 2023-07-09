

import sqlite3
import datetime


conexion = sqlite3.connect("cryptos.db")


conexion.execute("""
    CREATE TABLE IF NOT EXISTS bitcoin (
        moneda TEXT,
        precio REAL,
        fecha TEXT
    )
""")


precio_usd = obtener_precio_bitcoin("USD")
precio_gbp = obtener_precio_bitcoin("GBP")
precio_eur = obtener_precio_bitcoin("EUR")

# Obtenemos la fecha actual
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Insertar los datos en la tabla "bitcoin"
conexion.execute("""
    INSERT INTO bitcoin (moneda, precio, fecha)
    VALUES (?, ?, ?)
""", ("USD", precio_usd, fecha_actual))

conexion.execute("""
    INSERT INTO bitcoin (moneda, precio, fecha)
    VALUES (?, ?, ?)
""", ("GBP", precio_gbp, fecha_actual))

conexion.execute("""
    INSERT INTO bitcoin (moneda, precio, fecha)
    VALUES (?, ?, ?)
""", ("EUR", precio_eur, fecha_actual))

conexion.commit()

conexion.close()
