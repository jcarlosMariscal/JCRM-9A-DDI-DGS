import usuarios.usuario as modelo
class Acciones:

    def registro(self):
        print("Se procederá a realizar su registro en el sistema ...")

        nombre = input("¿Cuál es su nombre?: ")
        apellidos = input("¿Cuáles son sus apellidos?: ")
        email = input("¿Cuál es su Email?: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado  con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!!")

    def login(self):
        print("Identifiquese en el sistema...")

        email = input("Introduce tu Email: ")
        password = input("Introduce tu contraseña: ")
