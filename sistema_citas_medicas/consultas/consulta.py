import doctors.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consulta:
    def __init__(self,id_doctor, nom_paciente, telefono, edad):
        self.id_doctor = id_doctor
        self.nom_paciente = nom_paciente
        self.telefono = telefono
        self.edad = edad

    def agregar(self):
        sql = "INSERT INTO consultas VALUES(null,%s, %s, %s, %s, NOW())"
        consulta = (self.id_doctor, self.nom_paciente, self.telefono, self.edad)

        cursor.execute(sql, consulta)
        database.commit()
        return [cursor.rowcount, self]
    