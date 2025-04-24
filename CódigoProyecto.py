from bigtree import Node
from bigtree import print_tree

#Nodo Raíz
PlazaMoreno = Node(1)

#Nodos hijos de Raíz
PlazaSanMartin = Node(2, parent=PlazaMoreno)
PlazaDardoRocha = Node(3, parent=PlazaMoreno)
PlazaMaximoPaz = Node(4, parent=PlazaMoreno)
PlazaHipolitoYrigoyen = Node(5, parent=PlazaMoreno)
PlazaMalvinasArgentinas = Node(6, parent=PlazaMoreno)
PlazaAzcuenaga = Node(7, parent=PlazaMoreno)
PlazaPaso = Node(8, parent=PlazaMoreno)
PlazaItalia = Node(9, parent=PlazaMoreno)

#Hijos de la Plaza San Martín
PlazaRivadavia = Node(10, parent=PlazaSanMartin)

#Hijos de la Plaza Dardo Rocha
FiscaliadelEstado = Node(11, parent=PlazaDardoRocha)
PlazaMatheu = Node(12, parent=PlazaDardoRocha)
PlazaEspaña = Node(13, parent=PlazaDardoRocha)

#Hijos de la Plaza Maximo Paz
PlazaSaavedra = Node(14, parent=PlazaMaximoPaz)

#Hijos de la Plaza Hipolito Yrigoyen
PlazaSarmiento = Node(15, parent=PlazaHipolitoYrigoyen)
PlazaCastelli = Node(16, parent=PlazaHipolitoYrigoyen)
PlazaBrandsen = Node(17, parent=PlazaHipolitoYrigoyen)

#Hijos de la Plaza Malvinas Argentinas
PlazaVucetich = Node(18, parent=PlazaMalvinasArgentinas)

#Hijos de la Plaza Azcuenaga
Plaza19denoviembre = Node(19, parent=PlazaAzcuenaga)
PlazaAlberti = Node(20, parent=PlazaAzcuenaga)
PlazaGuemes = Node(21, parent=PlazaAzcuenaga)

#Hijos de la Plaza Paso
PlazaBelgrano = Node(22, parent=PlazaPaso)

#Hijos de la Plaza Italia
PlazaOlazabal = Node(23, parent=PlazaItalia)
PlazaAlsina = Node(24, parent=PlazaItalia)
DirecciondeMigraciones = Node(25, parent=PlazaItalia)

ubicaciones = {
    "Plaza Moreno": PlazaMoreno,
    "Plaza San Martín": PlazaSanMartin,
    "Plaza Dardo Rocha": PlazaDardoRocha,
    "Plaza Máximo Paz": PlazaMaximoPaz,
    "Plaza Hipólito Yrigoyen": PlazaHipolitoYrigoyen,
    "Plaza Malvinas Argentinas": PlazaMalvinasArgentinas,
    "Plaza Azcuénaga": PlazaAzcuenaga,
    "Plaza Paso": PlazaPaso,
    "Plaza Italia": PlazaItalia,
    "Plaza Rivadavia": PlazaRivadavia,
    "Fiscalía del Estado": FiscaliadelEstado,
    "Plaza Matheu": PlazaMatheu,
    "Plaza España": PlazaEspaña,
    "Plaza Saavedra": PlazaSaavedra,
    "Plaza Sarmiento": PlazaSarmiento,
    "Plaza Castelli": PlazaCastelli,
    "Plaza Brandsen": PlazaBrandsen,
    "Plaza Vucetich": PlazaVucetich,
    "Plaza 19 de noviembre": Plaza19denoviembre,
    "Plaza Alberti": PlazaAlberti,
    "Plaza Güemes": PlazaGuemes,
    "Plaza Belgrano": PlazaBelgrano,
    "Plaza Olazábal": PlazaOlazabal,
    "Plaza Alsina": PlazaAlsina,
    "Dirección de Migraciones": DirecciondeMigraciones
}

def mostrar_menu():
    print("=== Bienvenido a La Ruta del Tamal ===")
    print("Por favor, seleccione su ubicación para recibir el pedido:")
    for i, nombre in enumerate(ubicaciones.keys(), start=1):
        print(f"{i}. {nombre}")
    print("0. Salir")

def obtener_ruta_hasta_raiz(nodo):
    ruta = []
    while nodo:
        ruta.insert(0, str(nodo.name)) 
        nodo = nodo.parent
    return ruta

def recibir_pedido():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de su ubicación: ")
        if opcion == "0":
            print("¡Gracias por usar La Ruta del Tamal!")
            break
        try:
            opcion = int(opcion)
            ubicacion = list(ubicaciones.keys())[opcion - 1]
            nodo_destino = ubicaciones[ubicacion]
            ruta = obtener_ruta_hasta_raiz(nodo_destino)
            print(f"\n Pedido recibido para {ubicacion}")
            print(" Enviando domiciliario por la siguiente ruta:")
            print(" -> ".join(ruta))
            print("Pedido en camino...\n")
        except (IndexError, ValueError):
            print(" Opción inválida. Intente nuevamente.\n")

recibir_pedido()
