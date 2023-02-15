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
    def Buscar(self, cedula):
        copia = self.cabeza
        while copia != None:
            if int(copia.cedula) == int(cedula):
                return copia
            copia = copia.sig
        return None
    def Eleminar(self,cedula):

        if int(self.cabeza.cedula) == int(cedula):
            self.cabeza = self.cabeza.sig
            return True
        else:
            copia = self.cabeza
            anterior = copia
            while copia != None:
                if int(copia.cedula) == int(cedula):
                    anterior.sig = Nodo.sig
                    return True
                anterior = copia
                copia = copia.sig
        return False


if __name__ == "__main__":
    oLisSimpl = listasimples()
    while (True):
        print("----Menu-----\n "
              + "1. Agregar\n   "
              + "2. Listar\n"
              + "3. Buscar\n"
              + "4. Eleminar\n")
        numero = input("Ingrese la opcion: ")

        if numero =="1":
            nombre = input("Ingrese el nombre: ")
            Cedula = input("Ingrese la cedula: ")
            oNodo = Nodo(nombre, Cedula)
            oLisSimpl.agrega(oNodo)

        elif numero =="2":
             oLisSimpl.listar()

        elif numero == "3":
            cedula = input("Ingrese la cedula: ")
            Resultado = oLisSimpl.Buscar(cedula)
            if Resultado is not None:
                print(Resultado)
            else:
                print("Registro no encontrado")
        elif numero == "4":
            cedula = input("Ingrese la cedula: ")
            if oLisSimpl.Eleminar(cedula):
                print("Registro Borrado")
            else:
                print("Error en el proceso")



