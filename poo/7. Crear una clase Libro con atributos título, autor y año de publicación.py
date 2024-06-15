#7. Crear una clase Libro con atributos título, autor y año de publicación.

class Libro:
    def __init__ (self,titulo,autor,año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def Mostrar(self):
            print("El libro se titula",self.titulo,"su autor es",self.autor,"y se publico en el año",self.año)

Libro1 = Libro ("Gracias","Andres Manuel Lopez Obrador",2024)
Libro1.Mostrar()