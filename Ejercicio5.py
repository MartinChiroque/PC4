


import requests
import csv


def almacenar_txt(precio):
    with open("precios_bitcoin.txt", "a") as archivo:
        archivo.write(str(precio) + "\n")
        
        
import csv

def almacenar_csv(precio):
    with open("precios_bitcoin.csv", "a", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([precio])
        
        
precio = obtener_precio_bitcoin()
almacenar_txt(precio)
almacenar_csv(precio)
