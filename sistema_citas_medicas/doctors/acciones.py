import doctors.doctor as modelo

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