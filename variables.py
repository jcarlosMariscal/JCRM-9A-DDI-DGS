# Variables locales: se definen dentro de la función y no funcionan fuera de ella, solo estan disponibles dentro. A no ser que hagamos un return.hasattr
# Variables globales: son las que se declaran fuera de una funcion y estan disponibles fuera y dentro de ellas.

# Globales
frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres\n"
print(frase)
def holaMundo():
    frase = "Hola mundo !!!"
    print("Dentro de la función\n")
    print(frase)

    year = 2022
    print(year)

    # PERMITR EL ACCESO DESDE FUERA CON LA PALABRA RESERVADA global.
    global website 
    website = "wwww.uttehuacan.edu.mx/web"
    print("DENTRO: ", website)

    return "Dato devuelto " + str(year)

print(holaMundo())
print("FUERA: ", website)