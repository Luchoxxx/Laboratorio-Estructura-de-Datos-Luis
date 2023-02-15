##Listas circulares
#Creamos una clase
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class Cicular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self):
        return self.primero == None

    def AgregarInicio(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            axul = Nodo(dato)
            axul.siguiente = self.primero
            self.primero = axul
            self.ultimo.siguiente = self.primero


    def AgregarFinal(self,dato):

        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero

        else:
            axul = self.ultimo
            self.ultimo = axul.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        axul = self.primero
        while axul:
            print(axul.dato)
            axul = axul.siguiente
            if axul == self.primero:
                break

#Metodos para eleminar elementos de la lista circular
    def eleminarInicio(self,):

        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero
    def eleminarFinal(self):
        if self.Vacia():
            print("Esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            axul = self.primero
            while axul.siguiente != self.ultimo:
                 axul = axul.siguiente
            axul.siguiente = self.primero
            self.ultimo = axul


##EJECUCION
lista = Cicular()

lista.AgregarFinal(12)
lista.AgregarFinal(13)
lista.AgregarFinal(14)
lista.AgregarFinal(17)
lista.AgregarFinal(18)
lista.AgregarInicio(112)
lista.AgregarInicio(111)
lista.AgregarInicio(00)
lista.Recorrer()
lista.eleminarFinal()
print("Primero: ",lista.primero.dato)
print("ultimo: ",lista.ultimo.dato)
print(("ultimo.siguiente apunta a", lista.ultimo.siguiente.dato))
