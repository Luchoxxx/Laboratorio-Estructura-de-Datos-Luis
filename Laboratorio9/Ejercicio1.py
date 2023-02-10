# ESTRUCTUTA DE DATOS
# LISTAS SIMPLES

# Creamos una clase llamada Nodo
class mi_Nodo:

    def __init__(self, dato):
        # Creamos sus respectivos atributos

        self.dato = dato
        self.siguiente = None


class ListaEnlazadaCircular:

    def __init__(self):
        self.cabeza = None

    def agregaUltimo(self, dato):

        nodoNuevo = mi_Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nodoNuevo

            nodoNuevo.siguiente = self.cabeza

        else:
            temporal = self.cabeza

            while temporal.siguiente != self.cabeza:
                temporal = temporal.siguiente

            temporal.siguiente = nodoNuevo
            nodoNuevo.siguiente = self.cabeza

    def eleminaUltimo(self):

        if self.cabeza in None:
            return "La lista esta vacia"

        elif self.cabeza.siguiente == self.cabeza:

            temporal = self.cabeza
            self.cabeza = None

            return str(temporal.dato) + "Eliminado de la lista"

        else:

            temporal = self.cabeza

            while temporal.siguiente.siguiente != self.cabeza:
                temporal = temporal.siguiente

            temporal1 = temporal.siguiente
            temporal.siguiente = self.cabeza

            return str(temporal1.dato) + "Se elemino de la lista"

    def agregaPrimero(self, dato):

        nuevoNodo = mi_Nodo(dato)

        temporal = self.cabeza
        nuevoNodo.siguiente = self.cabeza

        if self.cabeza is not None:

            while temporal.siguiente != self.cabeza:
                temporal = temporal.siguiente

            temporal.siguiente = nuevoNodo

        else:
            nuevoNodo.siguiente = nuevoNodo

        self.cabeza = nuevoNodo

        # METODO QUE ELEMINA EL PRIMERO:

    def eliminaPrimero(self):

        if self.cabeza in None:

            return "Esta Vacia"
        elif self.cabeza.siguiente == self.cabeza:
            temporal = self.cabeza

            self.cabeza = None
            return str(temporal.dato) + "Se elemino de la lista"

        else:
            temporal = self.cabeza

            while temporal.siguiente != self.cabeza:
                temporal = temporal.siguiente

            temporal2 = self.cabeza
            self.cabeza = self.cabeza.siguiente
            temporal.siguiente = self.cabeza

            return str(temporal2.dato) + "se elemino de la lista"

    def muestraLista(self):

        if self.cabeza is None:
            return "Lista vacia"

        else:

            temporal = self.cabeza
            listavacia = []

            while temporal.siguiente != self.cabeza:
                listavacia.append(temporal.dato)

                temporal = temporal.siguiente
            listavacia.append(temporal.dato)

            return listavacia

        # Ejecucion del programa


# OBjeto
objeto_Lista = ListaEnlazadaCircular()
objeto_Lista.agregaUltimo("Luis")
objeto_Lista.eleminaUltimo()
objeto_Lista.muestraLista()
objeto_Lista.agregaPrimero("Alberto")
objeto_Lista.eliminaPrimero()
objeto_Lista.muestraLista()