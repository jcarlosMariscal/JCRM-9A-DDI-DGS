# Apartado 1: Repaso de conceptos básicos
""" numeros = [1,2,3,4,5]
print(numeros)
primeraPosicion = numeros[0]

longitud = len(numeros)
print(f"El primer valor es: {primeraPosicion}\nLa longitud de la lista es: {longitud}")
for num in numeros:
    print(num) """

# Apartado 2: Indexado y sublistas


""" lista = ["hola", "que", "tal", "como", "estas"]
print(lista)
ultimaPosicion = lista[-1]
print(ultimaPosicion)
penultimo = lista[-2]
print(penultimo)

sublista = lista[1:4]
print(sublista)
sublista = lista[:4]
print(sublista)
sublista = lista[2:]
print(sublista)

sublista = lista[-4:-1]
print(sublista) """

# Apartado 3: Comprobar si una lista tiene contiene o no un elemento
""" lista = ["hola", "que", "tal", "como", "estas"]
palabra = "como"
palabraDos = "mango"

if palabra in lista:
    print("La palabra pertenece a la lista")
if palabraDos not in lista:
    print("La palabra no pertenece a la lista")
""" 

# Apartado 4: Modificar elementos de una lista
"""lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]
print(lenguajes)
lenguajes[1] = "Angular"
print(lenguajes)
lenguajes[0] = lenguajes[0] + "++"
print(lenguajes)

lenguajes[2:4] = ["Anaconda", "Typescript"]
print(lenguajes)

lenguajes[4:5] = ["varios", "valores", "botella"]
print(lenguajes)"""

# Apartado 5: Métodos de las listas: Añadir elementos
# En python podemos utilizar métodos con las listas.
"""lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]
print(lenguajes)
lenguajes.insert(1, "C++")
print(lenguajes)

lenguajes.append("Typescript")
print(lenguajes)

lenguajesDos = ["Angular", "Vue", "React"]
lenguajes.extend(lenguajesDos)
print(lenguajes)
print(lenguajesDos)

lenguajesDos.extend(lenguajes)
print(lenguajesDos)"""

# Apartado 6: Métodos de las listas: Eliminar elementos
"""frutas = ["plátano", "kiwi", "papaya", "mango", "cereza"]
print(frutas)

frutas.pop()
print(frutas)

frutas.pop(0) #Retorna el valor
print(frutas)

frutas.remove("kiwi")
print(frutas)

del frutas[0]
print(frutas)

indice = frutas.index("mango")
print(indice)"""

# Apartado 7: Ejercicio
# ENUNCIADO: Tenemos un texto en donde queremos encontrar palabras clave. Las palabras clave pueden ser hasta 5 y debemos pedirselas al usuario y guardarlas en una lista.
# Si el usuario quiere poner menos de 5 palabras clave , deberá escribir fin para terminar de introducir los datos. Si el usuario introduce numeros o nada, deberemos eliminarlos de la lista antes de la búsqueda.
# En otra lista, debemos guardar un número de veces que aparece cada palabra clave  en nuestro texto. Por ejemplo, si la palabra clave son ordenador y portatil y aparecen 5 y 7 veces respectivamente, nuestras listas deberian ser asi: keywords[ordenador, portatil], ocurrencias[5, 7]

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 20/05/2022 ##### \n")

texto = """Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa.
Es muy importante que logremos teletrabajar efectivamente  y de manera autorregulada.
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior"""
palabras = []
ocurrencias = []

for limite in range(5):
    palabra = input("Introduce la palabra clave: ")
    if palabra == "fin":
        break
    else:
        palabras.append(palabra)

i = 0
while True :
    if i >= len(palabras):
        break
    if palabras[i] == '':
        palabras.pop(i)
    elif palabras[i].isnumeric():
        palabras.pop(i)
    else:
        i+=1
print(palabras)

texto = texto.split()
for x in range(len(palabras)):
    ocurrencias.append(0)
for text in texto:
    for p in palabras:
        if p == text:
            pos = palabras.index(p)
            ocurrencias[pos] += 1
            break
print(ocurrencias)
