#PROGRAma de Tareas
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class PilaTarea:
    def __init__(self):
        self.primeraTarea = None
        self.ultimaTarea = None
        self.size = 0

    def agregaTAREA(self, tarea):

        oNodo = Nodo(tarea)
        if self.primeraTarea == None:
            self.primeraTarea = oNodo
            self.ultimaTarea = oNodo

        else:
            oNodo.siguiente = self.primeraTarea
            self.primeraTarea.anterior = oNodo
            self.primeraTarea = oNodo

        self.size  = self.size + 1

        print("Tarea agregada al Inicio")

    def eliminaTAREA(self):

        if self.ultimaTarea == None:
            print("Lista vacia")
        else:
            tarea = self.ultimaTarea.dato
            self.ultimaTarea = self.ultimaTarea.anterior

            if self.ultimaTarea == None:
                self.primeraTarea = None
            else:
                self.ultimaTarea.siguiente = None
            self.size = self.size + 1

            print("Tarea eliminada")

    def MostrarTarea(self):

        if self.primeraTarea == None:
            print("Tarea vacia")
        else:
            print("Todas de forma inverza")
            actualTarea = self.primeraTarea

            while actualTarea != None:
                print(actualTarea.dato)
                actualTarea = actualTarea.siguiente

    def muestraTotalDeTareas(self):
        print(f"Hay un total de {self.size} tareas en la lista")

##Ejecucucion del programa

oTarea = PilaTarea()
bandera = True

while bandera:
    print("\nQué quieres hacer?")
    print("1. Agregar tarea al inicio de la lista")
    print("2. Eliminar tarea del final de la lista")
    print("3. Mostrar todas las tareas en forma invertida")
    print("4. Mostrar la cantidad total de tareas")
    print("5. Salir")

    respuesta = int(input("ingresa una opcion: "))

    if respuesta == 1:
        Tarea = input("Ingresa tarea: ")
        oTarea.agregaTAREA(Tarea)
    elif respuesta == 2:
        oTarea.eliminaTAREA()
    elif respuesta == 3:
        oTarea.MostrarTarea()
    elif respuesta == 4:
        oTarea.muestraTotalDeTareas()
    elif respuesta == 5 :
        print("Programa cerrado")
        break

