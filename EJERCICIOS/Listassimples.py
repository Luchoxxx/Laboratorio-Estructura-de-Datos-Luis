##Creamos una clase nodo
class Nodo:
    def __init__(self, nombre=None, cedula=None, sig=None):
        self.nombre = nombre
        self.cedula = cedula
        self.sig = sig

    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula)

class listasimples:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    # CREAMOS UNA FUNCION AGREGAR
    def agrega(self, elemento):

        if self.cabeza == None:
            self.cabeza = elemento

        if self.cola != None:
            self.cola.sig = elemento

        self.cola = elemento
    def listar(self):
        copia = self.cabeza

        while copia!= None:
            print(copia)
            copia = copia.sig

if __name__ == "__main__":
    oLisSimpl = listasimples()
    while (True):
        print("----Menu-----\n "
              + "1. Agregar\n"
              + "2. Listar\n")
        numero = input("Ingrese la opcion: ")

        if numero =="1":
            nombre = input("Ingrese el nombre: ")
            Cedula = input("Ingrese la cedula: ")
            oNodo = Nodo(nombre, Cedula)
            oLisSimpl.agrega(oNodo)

        elif numero =="2":
             oLisSimpl.listar()


