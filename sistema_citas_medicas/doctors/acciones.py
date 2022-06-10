import doctors.doctor as modelo
import consultas.acciones

class Acciones:
    def registro(self):
        print("Introduzca sus datos para el registro en el sistema.")

        nombre = input("¿Cuál es su nombre?: ")
        apellidos = input("¿Cuáles son sus apellidos?: ")
        telefono = input("¿Cuál es su número de teléfono?: ")
        nconsultorio = input("¿Cuál es su número de consultorio?: ")
        especialidad = input("¿Cuál es su especialidad?: ")
        email = input("¿Cuál es su Email?: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, telefono, nconsultorio, especialidad, email, password)
        registro = doctor.registrar()
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado  con el email {registro[1].email}")
        else:
            print("\nHa ocurrido un error, no se ha podido realizar su registro. Intente de nuevo más tarde.")

    def login(self):
        print("\nInicie sesión en el sistema")
        # try:
        email = input("Introduce tu Email: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor('','','','','',email, password)
        login = doctor.login()
        if email == login[6]:
            print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
            self.proximasAcciones(login)
        # except Exception as e:
        #     print(type(e)) - print(type(e).__name__)
        #     print("\nLogin incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, doctor):
        print("""
        Acciones disponibles:
            - Agregar consulta (a)
            - Listar consultas (l)
            - modificar consulta (m)
            - Eliminar consulta (e)
            - Salir (s)
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = consultas.acciones.Acciones()
        if accion == "a":
            # print("Vamos a agregar una consulta")
            hazEl.agregar(doctor)
            self.proximasAcciones(doctor) 
        elif accion == "l":
            print("Esta es la lista de consultas")
            hazEl.listar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "m":
            print("Vamos a modificar una consulta")
            hazEl.actualizar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "e":
            print("Vamos a eliminar una consulta")
            # hazEl.borrar(usuario)
            # self.proximasAcciones(usuario)
        elif accion == "salir":
            print("\nVuelva Pronto!!!")
            exit()
