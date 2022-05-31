# FUNCIONES: funcipon es un conjunto de instrucciones agruopadas bajo un nombre concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario

#def nombreDeLaFuncion(Parametros):
    #Bloque / Conjunto de instrucciones

## Llamar a la funcion: 
# nombreDeLaFuncion()

""" dfgdf """ """ - Shift + alt + a """

## EJEMPLO 1
print('######## Ejemplo 1 ########')
# Definir una función
def muestrameNombre():
    print('Victor')
    print('Maria')
    print('Pedro')
    print('Luisa')
    print('Cesar')
    print('Noemi')
    print('\n')
# Invocar la funcion
##### muestrameNombre()


## EJEMPLO 2
print("\n")
print('######## Ejemplo 2 ########')
nombre = "Carlos Mariscal"
cadena = ", es el contenido de la variable nombre"
def mostrarTuNombre():
    print(f"Tu nombre es: {nombre}{cadena}") #Es importante colocar f antes de la comilla
### mostrarTuNombre()

def mostrarMiNombre(nombre2, edad):
    print(f"Tu nombre es: {nombre2}")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
## mostrarMiNombre("Carlos Mariscal jej",15)
print("\n")

## nombre3 = input("Introduce tu nombre: ")
## edad = int(input("Introduce tu edad: "))
## mostrarMiNombre(nombre3, edad)

# EJEMPLO 3
print('######## Ejemplo 3: Funciones y parametros ########')
def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    for contador in range(11):
        operacion = numero * contador
        print (f"{numero} X {contador} = {operacion}")
    print("\n")
#numero = int(input("Introduce el numero para hacer la tabla: "))
#tabla(numero)

# EJEMPLO 3.1
print("\n")
print("------------------------------------------------------------")
""" for numero_tabla in range(1, 11):
    tabla(numero_tabla) """

# EJEMPLO 4
print('######## Ejemplo 4: Parametros opcionales ########')
def getEmpleado(nombre, dni= None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")
getEmpleado("Carlos Mariscal","3519210015")

print("\n")
# EJEMPLO 5: Parametros opcionales y return o devolver datos
print('######## Ejemplo 5: Parametros opcionales y return o devolver datos ########')
def saludame(name):
    saludo = f"Hola, saludos DDI - {name}"
    return saludo
print(saludame("Carlos"))


print("\n")
# EJEMPLO 6: 
print('######## Ejemplo 6: ########')
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\nResta: " + str(resta)
    else:
        cadena += "\nMultiplicacion: " + str(multiplicacion)
        cadena += "\nDivision: " + str(division)
    return cadena
print(calculadora(5, 5, False))

print("\n")
# EJEMPLO 7: 
print('######## Ejemplo 7: ########')
# EJERCICIO 7
print("\n ##### Ejemplo 7 #####\n")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto
def getApellidos(apellido):
    texto = f" y el apellido es: {apellido}"
    return texto
def devuelveTodo(nombre, apellido):
    texto = getNombre("Carlos") + "\n" + getApellidos("Mariscal") 
    return texto
#print(devuelveTodo("Carlos","Mariscal"))

# EJERCICIO 8: Funciones Lambda
print("\n ##### Ejemplo 8: Funciones Lambda (anónimasm pequeñas- que abarcan una sola linea) #####\n")
dime_el_year = lambda year: f"El año es: {year}"
print(dime_el_year(2034))