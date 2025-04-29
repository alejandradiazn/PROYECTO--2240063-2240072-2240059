class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class ListaParadas:
    def __init__(self):
        self.cabeza = None
    
    def vacio(self):
        if self.cabeza is None:
            print("No hay ninguna parada")
        else:
            print("Se encuentran paradas")
    
    def contar(self):
        contador = 0
        control = self.cabeza
        while control != None:
            contador += 1
            control = control.siguiente
        print(f"Hay un total de {contador} paradas")
    
    def imprimir(self):
        control = self.cabeza
        if control == None:
            print("No hay paradas en la lista.")
            return
        print("Listado de paradas:")
        while control != None:
            print(f"La parada {control.data}")
            control = control.siguiente
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def busqueda(self, dato):
        control = self.cabeza
        contador = 1 
        while control.data == dato or control == None:
             contador += 1
             control = control.siguiente
        if(control == None):
            print("La parada no se encunetra en la lista")
        else:
            print(f"La parada se encuentra en la posicion {contador}")
    
    def eliminarParada(self):
        if self.cabeza != None:
            print(f"Eliminando la parada: {self.cabeza.data}")
            self.cabeza = self.cabeza.siguiente
        else:
            print("No hay paradas para eliminar")

# Ejemplo de uso
lista_paradas = ListaParadas()
lista_paradas.agregar("Terminal Central")
lista_paradas.agregar("Avenida Principal")
lista_paradas.agregar("Plaza Mayor")
lista_paradas.agregar("Universidad")
lista_paradas.agregar("Estación Norte")

lista_paradas.imprimir()
lista_paradas.contar()
lista_paradas.busqueda("Plaza Mayor")
lista_paradas.eliminarParada()
lista_paradas.imprimir()
