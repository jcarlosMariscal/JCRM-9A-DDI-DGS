import consultas.consulta as modelo

class Acciones:
    def agregar(self, doctor):
        print(f"Ok {doctor[1]}!!! Vamos a agendar una nueva consulta...")

        nom_paciente = input("Introduce el nombre del paciente: ")
        telefono = input("Escribe el telefono: ")
        edad = input("Escribe su edad: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, telefono, edad)
        guardar = consulta.agregar()
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has agendado la consulta para el paciente: {consulta.nom_paciente}\n")
        else:
            print(f"\nNo se guardo tu nota, intentao más tarde: {doctor[1]}")
    
    def listar(self, doctor):
        print(f"{doctor[1]}: Estas son sus consultas: ")
        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()


        for consulta in consultas:
            print(f"{consulta[2]} - {consulta[3]} - {consulta[4]} - {consulta[5]}")

    def actualizar(self, doctor):
        print(f"Ok {doctor[1]}!!! Vamos a modificar una consulta...")

        nom_paciente = input("Introduce el nombre del paciente: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente)
        validar = consulta.validar()
        print(f"\nEste es el valor devuelto: {validar[0]}\n")
        if validar[0] != 0:
            self.modificar(doctor, nom_paciente)
        else:
            print(f"\nParece que no hay una consulta agendada para ese paciente, intentao más tarde: {doctor[1]}")

    def modificar(self, doctor,nombre):
        print(f"Ok {doctor[1]}!!! Escriba los nuevos datos del paciente {nombre}")

        nom_paciente = input("Introduce el nuevo nombre del paciente: ")
        telefono = input("Escribe el nuevo telefono: ")
        edad = input("Escribe la edad: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, telefono, edad, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han modificado los datos del paciente: {consulta.nom_paciente}. Presione (l) para listar las consultas y verificar el cambio\n")
        else:
            print(f"\nNo se guardo tu nota, intentao más tarde: {doctor[1]}")
    