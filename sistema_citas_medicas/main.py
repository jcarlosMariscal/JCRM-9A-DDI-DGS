from doctors import acciones

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
    print("login")
elif accion == "s":
    print("Vuelva pronto.")