class Camiseta:

    # print("\n### Juan Carlos Ramírez Mariscal - 9A - Desarrollo Para Dispositivos Inteligentes - 23/05/2022 ## \n")

    def __init__(self, marca, precio, talla, color): # Construye un objeto, inicializa la clase (constructor) - Self hace referencia al objeto que estamos instanciando
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color
        self.rebajada = False
    
    def aplicarDescuento(self, porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebajada = True
    
    def infoProducto(self):
        info = f"Descripción de la camiseta:\nMarca: {self.marca}\nPrecio: {self.precio:.2f}\nTalla: {self.talla}\nColor: {self.color}."
        if self.rebajada:
            info += "\nESTE PRODUCTO ESTÁ REBAJADA"
        return info

camiseta = Camiseta("Nike", 19.99, "S", "Lila")
camisetaAdidas = Camiseta("Adidas", 30, "M", "Azul")

"""print(camisetaAdidas.precio)
camisetaAdidas.aplicarDescuento(50)
print(camisetaAdidas.precio)

camiseta.aplicarDescuento(20)
print(camiseta.precio)"""
camiseta.aplicarDescuento(10)
camisetaAdidas.aplicarDescuento(50)

print(camiseta.infoProducto())
print("##########################")
print(camisetaAdidas.infoProducto())