import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"Ok {usuario[1]}!!! Vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Escribe el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se guardo tu nota, intentao más tarde: {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]}!!! Estas son tus notas: \n")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        # print(notas)

        for nota in notas:
            print("*********************************** ")
            print(f"{nota[2]} - {nota[3]}")
            print("*********************************** \n")