import datetime
import hashlib #Cifrar contraseñas en Python
import doctors.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:
    def __init__(self, nombre, apellidos, telefono, nconsultorio, especialidad, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.nconsultorio = nconsultorio
        self.especialidad = especialidad
        self.email = email
        self.password = password
    
    def registrar(self):
        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))
        print(f"""
            nombre: {self.nombre}
            apellidos: {self.apellidos}
            telefono: {self.telefono}
            nconsultorio: {self.nconsultorio}
            especialidad: {self.especialidad}
            email: {self.email}
            password: {self.password}
            cifrado: {cifrado.hexdigest()}
        """)

        sql = "INSERT INTO doctor VALUES (null, %s, %s, %s, %s, %s, %s, %s)"
        # newConsul = int(self.nconsultorio)
        doctor = (self.nombre, self.apellidos, self.telefono, self.nconsultorio, self.especialidad, self.email, cifrado.hexdigest())

        try:
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result