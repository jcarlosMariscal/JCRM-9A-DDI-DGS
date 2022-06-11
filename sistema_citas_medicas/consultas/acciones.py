import consultas.consulta as modelo

class Acciones:
    def agregar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]}  - Agendar nueva consulta")

        nom_paciente = input("Introduce el nombre del paciente: ")
        genero = input("Introduce su genero (M/F): ")
        edad = input("Introduce su edad: ")
        telefono = input("Introduce su telefono: ")
        fecha_consulta = input("Introduce la fecha para hacer la consulta [yyyy-mm-dd]: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, genero, edad, telefono, fecha_consulta)
        guardar = consulta.agregar()
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has agendado la consulta para el paciente: {consulta.nom_paciente}\n")
        else:
            print(f"\nNo se pudo agendar la consulta, intente más tarde {doctor[1]}")
    
    def listar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Detalles de consultas agendadas")
        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()


        for consulta in consultas:
            print(f"""
    Paciente: {consulta[2]}
    Genero: {consulta[3]}
    Edad: {consulta[4]}
    Telefono: {consulta[5]}
    Para el: {consulta[6]}
    Agendado el: {consulta[7]}
    -----------------------------------------""")

    def actualizar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Modificar una consulta")

        nom_paciente = input("Introduce el nombre del paciente a modificar: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente)
        validar = consulta.validar()
        if validar[0] != 0:
            self.modificar(doctor, nom_paciente)
        else:
            print(f"\nNo se encontró ninguna consulta con el nombre del pacientte [{nom_paciente}], verifique la ortografía : {doctor[1]}")

    def modificar(self, doctor,nombre):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Escriba a continuación los nuevos datos de {nombre}")

        nom_paciente = input("Introduce el nuevo nombre del paciente: ")
        genero = input("Introduce su genero (M/F): ")
        edad = input("Introduce su edad: ")
        telefono = input("Introduce su telefono: ")
        fecha_consulta = input("Introduce la fecha para hacer la consulta [yyyy-mm-dd]: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, genero, edad, telefono, fecha_consulta, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han modificado los datos del paciente: {consulta.nom_paciente}. Presione (l) para listar las consultas y verificar el cambio\n")
        else:
            print(f"\nNo se pudo modificar la consulta agendada del paciente, intente más tarde: {doctor[1]}")
    
    def eliminar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Borrar una consulta de la agenda")
        nom_paciente = input("Introduce el nombre del paciente para eliminar la consulta: ")

        nota = modelo.Consulta(doctor[0], nom_paciente)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"\nSe eliminó la consulta de: {nota.nom_paciente}")
        else:
            print("\nNo se puedo eliminar la consulta, intenta más tarde...")