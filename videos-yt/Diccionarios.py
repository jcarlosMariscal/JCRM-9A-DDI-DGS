# EJERCICIO: Buscar productos - Tenemos varios productos, el usuario mediante el nombre de un producto puede consultar su precio y sus unidades en stock

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 22/05/2022 ##### \n")

pal = ""
productos = [
    {"nombre": "zapatos", "precio": 120.00, "stock": 21},
    {"nombre": "playeras", "precio": 100.00, "stock": 10},
    {"nombre": "tenis", "precio": 250.00, "stock": 45}
    ]

def askForInfo(nombre):
    for producto in productos:
        if(producto["nombre"] == nombre):
            return producto["precio"], producto["stock"]
            break
    else:
        return 0,0

nom = ""
while nom != "salir":
    nom = input("\nIntroduce el producto que estás buscando: ")
    precio, stock = askForInfo(nom)
    if precio == 0 and stock == 0:
        print("Parece que el producto que buscas no existe")
    else:
        print(f"\nEl producto {nom} vale {precio} pesos y tenemos {stock} unidades\n")












# Diccionarios
# Apartado 1: conceptos básicos

# Los diccionarios son conjuntos de elementos con la estructura clave-valor. Cada elemento tiene estos valores, las claves pueden ser string o int. De cualquier tipo
"""alejandro = {
    "Nombre": "Alejandro", 
    "Edad": 32, "Ciudad": 
    "Barcelona", 
    "aficiones":["lectura", "cine", "videojuegos"]
    }
print(alejandro)
ana = {"Nombre": "And", "Edad": 42, "Ciudad": "Madrid", "aficiones":["pesca", "natacion", "escritura", "cantar"]}
print(ana)

trabajadores = {0: alejandro, 1: ana}
print("\n")
print(trabajadores)

print(f"La longitud del diccionario de alejandro es: {len(alejandro)}")
print(f"La longitud del diccionario de trabajadores es: {len(trabajadores)}")"""

"""print("Ejemplo: claves duplicadas")
a = {"año": 1990, "año": 2003, "otraClave": 5686, "año":2000} # Se queda con el ultimo elemento
print(a)"""

# Apartado 2: Añadir, eliminar y modificar elementos de un diccionario
"""from this import d
from tkinter import N


alejandro = {
    "Nombre": "Alejandro", 
    "Edad": 32, "Ciudad": 
    "Barcelona", 
    "aficiones":["lectura", "cine", "videojuegos"]
    }
print(alejandro)
alejandro["cargo"] = "CEO"
print(alejandro)

alejandro.update({"sueldo": 900000, "vacaciones": "muchas"})
print(alejandro)

print("Eliminar")
del alejandro["vacaciones"]
valor = alejandro.pop("cargo")
print(alejandro)
print(f"El valor eliminado es: {valor}")

print("acceder a un elemento")
edad = alejandro["Edad"]
print(edad)"""

# Apartado 3: Listas de claves y valores - Podemos obteneer una lista tanto de las claves como de los valores que conforman un diccionario
"""alejandro = {
    "Nombre": "Alejandro", 
    "Edad": 32, "Ciudad": 
    "Barcelona", 
    "aficiones":["lectura", "cine", "videojuegos"]
    }
for clave, valor in zip(alejandro.keys(), alejandro.values()):
    print(f"{clave} -> {valor}")

for clave, valor in alejandro.items():
    print(f"{clave} === {valor}")"""