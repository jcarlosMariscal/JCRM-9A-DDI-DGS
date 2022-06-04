import usuarios.usuario as modelo
import notas.acciones 
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
        print("\nIdentifiquese en el sistema...")

        try:
            email = input("Introduce tu Email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e)) - print(type(e).__name__)
            print("\nLogin incorrecto!! Intentalo más tarde")
            
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - Crear nota (crear)
            - Mostrar notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = notas.acciones.Acciones()
        if accion == "crear":
            # print("Vamos a crear una nota")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario) 
        elif accion == "mostrar":
            # print("Vamos a mostrar las notas")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar una nota")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print("\nVuelva Pronto!!!")
            exit()