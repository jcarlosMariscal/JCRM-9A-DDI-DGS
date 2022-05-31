# Ejercicio (mini): TEnemos un String compuesto por números enteros.
# Debemos sumar su valor uno a uno y mostrar por pantalla la suma total de los numeros.

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 20/05/2022 ##### \n")

numeros = "684615461"
suma = 0
for num in numeros:
    num = int(num)
    suma += num
print(f"La suma de los numeros es: {suma}")




# Cadena de caracteres o Strings
# Apartado 1: Repaso de conceptos básicos

"""texto = "\nHola, ¿Qué tal?"
print(texto)
texto = 'Hola, ¿Qué tal?'
print(texto)

comillasSimples = "El personaje dijo 'con esto terminamos esta actividad'\n"
print(comillasSimples)

stringConFormato = 
==================== TEXTO FORMATEADO =======================
El texto formateado:
    1.- Poner saltos de línea.
    2.- Poner sangrías.
Y mostrarlo así por pantalla.\n

print(stringConFormato)"""

"""valorEntero = 5
valorDecimal = 3.14
valorBooleano = False
print("Tipos de datos originales")
print(type(valorEntero))
print(type(valorDecimal))
print(type(valorBooleano))

valorEntero = str(valorEntero)
valorDecimal = str(valorDecimal)
valorBooleano = str(valorBooleano)
print("Tipos de datos mofificados")
print(type(valorEntero))
print(type(valorDecimal))
print(type(valorBooleano))

texto = "0123456789"
print("La longitud del texto es: " )
print(len(texto))

texto1 = "01234"
texto2 = "56789"
texto3 = "Los valores son: " + texto1 + texto2
print(texto3) """

# Apartado 2: Los strings son listas: Similares a las listas
# texto = "0123456789"
# print(texto[0])
