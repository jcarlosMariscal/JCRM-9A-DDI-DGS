# Capítulo 11: Tuplas
# Apartado 1: Tuplas - Conceptos básicos . Las tuplas son conjuntos ordenados de datos que no se pueden modificar

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 23/05/2022 ##### \n")

mitupla = ("Bad Bunny", "Anuel", "Daddy Yankee", "Farruko")
print(mitupla)
print(f"\nLa longitud de mi tupla es: {len(mitupla)}")

for cantante in mitupla:
    print(f"\nCantante número: {mitupla.index(cantante)+1} es {cantante}")

# Apartado 2: Indexado de Tuplas - Podemos indexar los elementos  de una tupla de la misma forma que las listas.
mitupla = ("Bad Bunny", "Anuel", "Daddy Yankee", "Farruko")
print(mitupla)
primero = mitupla[0]
ultimo = mitupla[-1]

suptupla = mitupla[1:3]
print(f"El primer cantante es: {primero}")
print(f"El ultimo cantante es: {ultimo}")
print(suptupla)

# Apartado 3: Modificar tuplas - No podemos modificar directamente una tupla. Veremos qué errores ocurren y cómo transformar una tupla y viceversa.
"""mitupla = ("Bad Bunny", "Anuel", "Daddy Yankee", "Farruko")
print(mitupla)
# del mitupla[1]
# mitupla.append("El nuevo")

milista = list(mitupla) # Convertir tupla a lista
print(milista)
print(type(milista))
milista.append("Don Omar")
print(milista)

mitupla = tuple(milista) # Convertir lista a tupla
print(mitupla)
"""

# Apartado 4: Empaquetar y desempaquetar tuplas - De la misma manera que podemos agrupar múltiples variables en una tupla (empaquetar), también podemos asignar  cada elemento de una tupla a una variable distinta.
"""mitupla = ("Bad Bunny", "Anuel", "Daddy Yankee", "Farruko")
print(mitupla)
artista1 = "ctangana"
artista2 = "Duki"

nuevaTupla = (artista1, artista2) # EMPAQUETAR
print(nuevaTupla)

(cantante1, cantante2, cantante3, cantante4) = mitupla # DESEMPAQUETAR
print(f"Primer cantante: {cantante1}.\nSegundo cantante: {cantante2}")

(cantante1, *cantatntesVarios) = mitupla
print(cantante1)
print(cantatntesVarios)

mitupla2 = mitupla + nuevaTupla
print("\n")
print(mitupla2)

(cantante1, *varios,ultimocantante) = mitupla2
print("\n")
print(cantante1)
print(varios)
print(ultimocantante)"""

# Apartado 5: *Extra* Listas de Tuplas - Podemos crear listas cuyos elementos sean tuplas. De esta forma, podemos iterar sobre las diversas tuplas  y además desempaquetar sus elementos.
comida = [("primero","macarrones"), ("segundo", "pollo"), ("postre", "flan")]
for numero, plato in comida:
    print(f"{numero} -> {plato}")