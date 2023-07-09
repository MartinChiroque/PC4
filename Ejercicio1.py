



#Hola, mira me sale el error de la biblioteca, lo instale tal y como lo pusiste en la tarea
#pero creo que es cosa de mi laptop, o algun problema con el programa. Recuerdas que en la primera clase
#te dije que no podia instalar la extension de phyton y me hiciste compartir pantalla, habrá algun problema seguro y no me deja
#xfa tenme en consideración, recien tuve tiempo hoy pero no me fue suficiente, busque solucion al problema en chatgpt
#y me decia que debo dar permisos avanzados y unas cosas mas que la verdad no entiendo. Muchas gracias, tenme en consideracion xfa
#todas las tareas anteriores si las he enviado a tiempo

import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException:
        print("Error al obtener el precio de Bitcoin")
        return None

def mostrar_precio_en_usd(cantidad_bitcoins):
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_usd = cantidad_bitcoins * precio_bitcoin
        print(f"El costo actual de {cantidad_bitcoins:.4f} Bitcoins en USD es: {costo_usd:,.4f}")


n = float(input("Ingrese la cantidad de Bitcoins que posee: "))

mostrar_precio_en_usd(n)
