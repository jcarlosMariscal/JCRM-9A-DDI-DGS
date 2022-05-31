# Capitulo 10: Funciones - Capítulo 2 : argumentos arbitrariosy keyword arguments
# ARGUMENTO ARBITRARIOS

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 22/05/2022 ##### \n")

def maximo(*args):
    maximo = args[0]
    for numero in args[1: ]:
        if(numero > maximo):
            maximo = numero
    return maximo
print(maximo(10,25,69,23,52,33,2.6,6.5))
print(maximo(55,-2,-5888, 51,8))

def formatoDescarga(tipo, *args):
    numArgs = len(args)
    if tipo == "video":
        if numArgs == 0:
            print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}\n")
        elif numArgs == 1:
            print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}\n-Resolución: {args[0]}\n")
        elif numArgs == 2:
            print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}\n-Resolución: {args[0]}\n-FPS: {args[1]}\n")
    elif tipo == "audio":
        print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}\n")
    else:
        print("El formato es incorrecto")

formatoDescarga("video", 720)
formatoDescarga("video", 1080, 60)
formatoDescarga("audio")

# KEYWORD ARGUMENTS - De esta forma conseguimos que el orden de los argumentos sean indiferentes
def crearPersonaje(clase, raza, nombre):
    print(f"{nombre.upper()} es un {clase} de raza {raza}")

crearPersonaje(nombre="Ata", clase="Guerreo", raza="Saiyajin")
crearPersonaje("mago", "elfo", "mandalorian")

# Apartado 3: Keyword Arbitrary Arguments - Se utilizan cuando no sabemos cuantos argumentos de palabras clave vamos a recibir
def printKwargs(**kwargs):
    print("\n")
    print("Los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print(f"{clave} --->>> {valor}")
printKwargs(nombre="Ata", clase="Guerreo", raza="Saiyajin", mascota="Dragon", clan="Dioses")
printKwargs(clase="mago", raza="elfo", nombre="mandalorian")


# Apartado 4: Combinación de todos los anteriores - Se pueden usar conjuntamente en una misma funcion
def crearPer(nombre, *args, **kwargs):
    descripcion =  f"\n##### {nombre.upper()} #####\n\n"

    descripcion +=  f"##### DESCRIPCIÓN #####\n\n"
    for clave, valor in kwargs.items():
        descripcion += f"- {clave} ---->>> {valor}\n"

    descripcion +=  f"##### HABILIDADES #####\n\n"
    for skill in args:
        descripcion += f"- {skill}\n"
    return descripcion

personaje = crearPer("Dandelion", "ataque fuerte", "bola de fuego", "salto doble", "ataque tres", clase="mago", raza="No-muerto",mascota="Serpiente")
print(personaje)