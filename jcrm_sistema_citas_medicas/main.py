from doctores import acciones

print("""
Seleccione una acción:
    - Registro (r)
    - Login (l)
    - Salir (s)
""")
hazEl = acciones.Acciones()

accion = input("¿Qué quiere hacer?: ")
if accion == "r":
    hazEl.registro()
elif accion == "l":
    hazEl.login()
elif accion == "s":
    print("\nVuelva pronto.")
else:
    print("¡¡¡ La opción seleccionada es inválida!!!")