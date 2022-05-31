import sqlite3 # Importar módulo

print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 24/05/2022 ##### \n")

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"descripcion TEXT,"+
"precio INT(255)"+
")")

# Guardar cambios
conexion.commit()

# Insertar Datos
cursor.execute("INSERT INTO productos VALUES (null,'Primer producto','Descripción de mi producto',550)")
cursor.execute("INSERT INTO productos VALUES (null,'Segundo producto','Descripción de mi producto',300)")

# Borrar datos
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de una sola instrucción
productos = [
    ("Ordenador Portatil", "Buena calidad", 700),
    ("Teléfono Móvil", "Xaomi 7", 140),
    ("Ordenador Portatil", "Para Windows", 80),
    ("Tablet 15", "Samsung", 300)
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio = 768 WHERE precio = 80")

# Listar datos - registros
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
# print(cursor)
productos = cursor.fetchall()
# print(productos)
    
# for producto in productos:
#     print(producto)

for producto in productos:
    print("ID: ",producto[0])
    print("Titulo: ",producto[1])
    print("Descripción: ",producto[2])
    print("Precio: ",producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchall()
print("\n *************** SELECT titulo ****************")
print(producto)
# Cerrar Conexión
conexion.close