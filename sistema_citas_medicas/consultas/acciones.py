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
            print(f"\nPerfecto! Has agendado la consulta para el paciente: {consulta.nom_paciente}")
        else:
            print(f"\nNo se guardo tu nota, intentao más tarde: {doctor[1]}")
    
    