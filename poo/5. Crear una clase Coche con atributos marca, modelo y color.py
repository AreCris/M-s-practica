#5. Crear una clase Coche con atributos marca, modelo y color.

class Coche:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def Mostrar(self):
          print("la marca del coche es ",self.marca,"el color es",self.color,"y el modelo es",self.modelo)

Coche1 = Coche("Nisan","Tzuru","blanco")
Coche1.Mostrar()