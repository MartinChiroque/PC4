



class TablaMultiplicar:
    def crear_tabla(self):
        numero = self.solicitar_numero()
        contenido = self.generar_contenido(numero)
        self.guardar_tabla(numero, contenido)
    
    def mostrar_tabla_completa(self):
        numero = self.solicitar_numero()
        try:
            contenido = self.leer_tabla(numero)
            self.mostrar_contenido(contenido)
        except FileNotFoundError:
            print(f"El fichero tabla-{numero}.txt no existe.")
    
    def mostrar_linea_tabla(self):
        numero = self.solicitar_numero()
        linea = self.solicitar_linea()
        try:
            contenido = self.leer_tabla(numero)
            self.mostrar_contenido(contenido[linea - 1])
        except FileNotFoundError:
            print(f"El fichero tabla-{numero}.txt no existe.")
    
    def solicitar_numero(self):
        while True:
            try:
                numero = int(input("Introduce un número entre 1 y 10: "))
                if numero < 1 or numero > 10:
                    raise ValueError
                return numero
            except ValueError:
                print("Error: Debes introducir un número entero entre 1 y 10.")
    
    def solicitar_linea(self):
        while True:
            try:
                linea = int(input("Introduce el número de línea: "))
                if linea < 1 or linea > 10:
                    raise ValueError
                return linea
            except ValueError:
                print("Error: Debes introducir un número entero entre 1 y 10.")
    
    def generar_contenido(self, numero):
        contenido = []
        for i in range(1, 11):
            contenido.append(f"{numero} x {i} = {numero * i}")
        return contenido
    
    def guardar_tabla(self, numero, contenido):
        with open(f"tabla-{numero}.txt", "w") as archivo:
            archivo.write("\n".join(contenido))
        print(f"La tabla de multiplicar de {numero} se ha guardado en tabla-{numero}.txt.")
    
    def leer_tabla(self, numero):
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.readlines()
        return contenido
    
    def mostrar_contenido(self, contenido):
        for linea in contenido:
            print(linea.strip())


def menu():
    tabla = TablaMultiplicar()
    while True:
        print("===== Menú =====")
        print("1. Crear tabla de multiplicar")
        print("2. Mostrar tabla completa")
        print("3. Mostrar línea de la tabla")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            tabla.crear_tabla()
        elif opcion == "2":
            tabla.mostrar_tabla_completa()
        elif opcion == "3":
            tabla.mostrar_linea_tabla()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Introduce un número del 1 al 4.")


if __name__ == "__main__":
    menu()
