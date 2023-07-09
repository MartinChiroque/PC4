



#aqui sigo teniendo el mismo problema que el ejercicio anterior con la biblioteca
# me subraya el "import pryfiglet"

from pyfiglet import Figlet
import random

def obtener_fuente():
    fuente = input("Ingrese el nombre de una fuente (dejar en blanco para seleccionar una aleatoria): ")
    if not fuente:
        fuentes_disponibles = pyfiglet.Figlet.getFonts()
        fuente = random.choice(fuentes_disponibles)
    return fuente

def obtener_texto():
    texto = input("Ingrese un texto: ")
    return texto

def imprimir_texto_en_fuente(fuente, texto):
    figlet = pyfiglet.Figlet(font=fuente)
    texto_en_fuente = figlet.renderText(texto)
    print(texto_en_fuente)

# Obtener la fuente a utilizar
fuente = obtener_fuente()

# Obtener el texto ingresado por el usuario
texto = obtener_texto()

# Imprimir el texto en la fuente apropiada
imprimir_texto_en_fuente(fuente, texto)
