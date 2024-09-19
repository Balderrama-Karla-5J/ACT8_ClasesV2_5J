print("Clases v2 Balderrama Karla ")
# Zona de clases 
class Datos:
    # El constructor es una funcion
    def __init__(self, estatura, peso ):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
      print(f"Tu estatura es de: {self.estatura}mts, su peso {self.peso}kg")
    def mi_lista(self):
        Animales=[ "Perros", "Gatos", "Hurones", "Leones"]
        print(Animales)
        for x in Animales:
            print(x)
    def mi_tupla(self):
        sabores =("Vainilla", "Chocolate", "Fresa")
        for s in sabores:
            print(s)
    def mi_set(self):
        colores = {"Azul", "Amarillo", "Verde", "Morado"}
        for c in colores:
            print(c)
    def mi_diccionario(self):
        galletas = { "Esencia:" : "Vainilla", "Forma:": "Dinosaurio", "Glaseado:": "Real"}
        for g, a in galletas.items():
            print(g,a)
#Creacion de objeto
info = Datos(1.54, 45)

# Utilizando el obj. --> info
info.mostrar_datos()
print("Lista de Animales --Balderrama Karla")
info.mi_lista()
print("Lista de Sabores de Helado-- Balderrama Karla")
info.mi_tupla()
print("Colores favoritos -- Balderrama Karla ")
info.mi_set()
print("Info galletas -- Balderrama Karla ")
info.mi_diccionario()