""" Listas (array)
Son colecciones  o conjuntos de datos/valores, bajo un único nombre. Para acceder a esos valores podemos un indice numerico """

pelicula = "Batman"
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
year = list(range(2020, 2050))
variada = ["Aurora", 30, 4.4, True, "Dirección"]
print(peliculas)
print(cantantes)
print(year)
print(variada)

# Indices
peliculas = ["Batman", "Spiderman", "Doctor Strange"]
cantantes = list(("2Pac", "Drake", "Jennifer Lopez"))

# Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

pelicula = "Otra cosa"
peliculas[1] ="Gran Totrino"
peliculas[2] ="El hobbit"

print(peliculas)

# Añadir elementos a una lista

cantantes.append("Kase O")
cantantes.append("Natos y Waor")
print("\n")
print(cantantes)

# Recorrer lista
print("\n##### Listado de Peliculas con For ######")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}.- {pelicula}.")

# Recorrer lista
print("\n##### Listado de Peliculas con While ######")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}.- {pelicula}.")


# Listas multidimensionales
print("\n##### Listas Multidimensionales ######")
contactos = [
    [
        'Antonio',
        'a@a'
    ],
    [
        'Luis',
        'l@l'
    ],
    [
        'Salvador',
        's@s'
    ],
]
print(contactos[1][0])