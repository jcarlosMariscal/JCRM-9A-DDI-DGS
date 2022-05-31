# Herencia simple, jerarquica, múltiple, multinivel
class Persona:

# print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 23/05/2022 ##### \n")

    def __init__(self, name, edad, DNI):
        self.nombre = name
        self.edad = edad
        self.DNI = DNI
    def presentarse(self):
        print(f"¡Hola! Me llamo {self.nombre} y tengo {self.edad} años")

oscar = Persona("Oscar", 23, "368DF5G528FDF")
oscar.presentarse()
print(oscar.DNI)

# ----------------------------- HERENCIA MULTIPLE ----------------------------
class Trabajador(Persona):
    # pass # No hace nada xd
    def __init__(self, nombre, edad, DNI, sueldo, cargo, empresa):
        super().__init__(nombre,edad, DNI)
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa
        self.colorPelo = "negro"

    def calcularSueldoAnual(self):
        return 12*self.sueldo+3000

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, universidad, curso, asignaturas):
        super().__init__(nombre, edad, DNI)
        self.universidad = universidad
        self.curso = curso
        self.asignaturas = asignaturas
    
    def describirse(self):
        print(f"""¡Hola soy {self.nombre}!. Tengo {self.edad} años y estudio en la {self.universidad}.
        Estoy en el curso {self.curso}""")

"""trabajador = Trabajador("Carlos", 33, "55626923266H", 1600, "Task", "Google")
trabajador.presentarse()
print(trabajador.calcularSueldoAnual())"""

estudiante = Estudiante("María", 20, "5566666F", "Universidad Tecnológica de Tehuacán", 3, ["programación", "cálculo", "física"])
estudiante.describirse()