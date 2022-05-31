import datetime
import hashlib #Cifrar contraseñas en Python
import usuarios.conexion as conexion

# Llamar la clase conectar
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES (null, %s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
    
    def identificar(self):
        # Login de usuarios
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result
