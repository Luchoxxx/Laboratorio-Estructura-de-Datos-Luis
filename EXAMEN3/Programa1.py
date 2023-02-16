#Lista de compras


#Creamos una clase Nodo
class Nodo:
    def __init__(self,producto):
        self.producto = producto
        self.siguiente = None

class listacompra:

    def __init__(self):
        self.primeracompra = None
        self.ultimaCompra = None

    def CompraVacia(self):
        return self.primeracompra == None

    def AgregaCompraInicio(self, producto):

        if self.CompraVacia():
            self.primeracompra = self.ultimaCompra = Nodo(producto)
            self.ultimaCompra.siguiente = self.primeracompra

        else:
            variable = Nodo(producto)
            variable.siguiente = self.primeracompra
            self.primeracompra = variable
            self.ultimaCompra.siguiente = self.primeracompra

    def AgregaCompraFinal(self, producto):

        if self.CompraVacia():
            self.primeracompra = self.ultimaCompra = Nodo(producto)
            self.ultimaCompra.siguiente = self.primeracompra
        else:
            variable = self.ultimaCompra
            self.ultimaCompra = variable.siguiente = Nodo(producto)
            self.ultimaCompra.siguiente = self.primeracompra

    def MostrarCompra(self):
        variable = self.primeracompra

        while variable:
            print(variable.producto)
            variable = variable.siguiente

            if variable == self.primeracompra:
                break
    def EleminarProductosInicio(self):

        if self.CompraVacia():
            print("Compra vacia")

        elif self.primeracompra == self.ultimaCompra:
            self.primeracompra = self.ultimaCompra = None

        else:
            self.primeracompra = self.primeracompra.siguiente
            self.ultimaCompra.siguiente = self.primeracompra

### EJECUCCION DE PROGRAMA

if __name__ == "__main__":

    oCompra = listacompra()
    bandera = True
    while bandera:
        print("PROGRAMA DE COMPRA\n" +
              "1.Agrega producto\n"+
              "2.Elemina mi compra Inicio")

        numero = int(input("Ingrese una opcion: "))
        if numero == 1:
            producto = input("Ingrese el producto: ")
            oNodo = Nodo(producto)
            oCompra.AgregaCompraFinal(oNodo)
        if numero == 2:
            producto = input("Ingrese producto: ")
            if oCompra.primeracompra(producto):
                print("Compra brorrada")

            else:
                print("Error en el proceso")




