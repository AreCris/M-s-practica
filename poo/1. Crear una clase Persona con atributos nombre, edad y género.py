#1. Crear una clase Persona con atributos nombre, edad y género.

class Persona:
    def __init__(self,nombre,edad,genero) :
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def Presentar(self):
            print("hola, mi nombre es",self.nombre,"tengo",self.edad,"años","mi genero es",self.genero)

Persona1 = Persona("Cristofer",19,"Masculino")
Persona1.Presentar()