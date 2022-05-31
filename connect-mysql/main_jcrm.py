# pip install mysql-connector-python
import mysql.connector

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 24/05/2022 ##### \n")

# Realizar conexión a la BD
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "jcrm_python"
)

# Ver si la conexión ha sido correcta
# print(database)

# Crear la Base de Datos
cursor = database.cursor(buffered=True)
# cursor.execute("CREATE DATABASE jcrm_python")
"""cursor.execute("CREATE DATABASE IF NOT EXISTS jcrm_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)"""

# CREAR TABLAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca VARCHAR(40) not null,
    modelo VARCHAR(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES;")
for table in cursor:
    print(table)

# Insertar datos en una tabla MYSQL
# cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500.00)")
coches = [
    ('Seat', 'Ibiza', 5000.00),
    ('Renault', 'Clio', 15000.00),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000.00)
]

# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()

# Consulta a la tabla - select
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
result = cursor.fetchall()

print(result)
print("\n----- Todos mis coches -------\n")
for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone() # Traer el primero que encuentre
print(coche)

# Borrar registro
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "borrados!!!")

# Actualizar datos de un registro en MYSQL
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()
print(cursor.rowcount, "Actualizados!!!")