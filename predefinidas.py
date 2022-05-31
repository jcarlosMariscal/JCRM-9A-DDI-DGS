# Funciones predefinidas

nombre = "Mary Sagnite"
# funciones generales
print(type(nombre))

# Detectar typado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variables no es un número con decimales")

# Limpiar espacios 
frase = "    Mi   contenido es   divertido    "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2022
print(year)

# del year
print(year)

# MANUAL DE PYTHON
# https://docs.python.org/es/3.9/index.html


# Comprobar variable vacía
text = " ff "
if len(text) <= 0:
    print("La variables está vacia")
else: 
    print("La variable tiene contenido de", len(text))

# Encontrar caracteres
otro = "La vida es bella"
print(otro.find("vida"))

# Reemplaza palabras en un string
nueva_frase = otro.replace("vida", "muerte")
print(nueva_frase)

# Mayusculas y minusculas
print("\n",nombre)
print("\n",nombre.lower())
print("\n",nombre.upper())