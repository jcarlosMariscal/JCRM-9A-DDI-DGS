
# print("\n##### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 27/05/2022 ##### \n")

"""
Proyecto Python + MySQL:
    1. Abrir el asistente.
    2. Login y registro
    3. Si elegimos registro, creará un usuario en la BD.
    4. Si elegimos login, identificará al usuario y nos preguntará los datos
    5. Crear nota, mostrar notas,  o borrarlas
"""
from usuarios import acciones
# import usuarios.acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")
hazEl = acciones.Acciones()

accion = input("¿Qué quiere hacer?: ")
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
