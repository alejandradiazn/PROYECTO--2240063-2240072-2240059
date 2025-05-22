import igraph as ig
from igraph import Graph, plot
import cairo

import scipy.io as sio
import numpy as np

edgelist =[(0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,1), (0,2)
           , (1,0), (1,8), (1,9), (1,2), (2,3), (2,0), (2,1), (2,9)
           , (2,10), (2,11), (2,12), (2,13), (3,4), (3,0), (3,2)
           , (3,13), (4,16), (4,17), (4,5), (4,0), (4,3), (4,13)
           , (4,14), (4,15), (5,17), (5,6), (5,0), (5,4), (6,0)
           , (6,7), (6,17), (6,20), (6,19), (6,18), (6,17), (6,5) # se termino el renglon, iniciar en el siguiente
           , (7,21), (7,6), (7,0), (7,8), (8,0), (8,7), (8,21), (8,22)#
           , (8,9), (8,23), (8,24), (9,1), (9,2), (9,8),(9,24), (9,10)#
           , (10,2), (10,9), (10,11), (11,2), (11,10), (11,12), (12,11)#
           , (12,2), (12,13), (13,12), (13,2 ), (13,3), (13,4), (13,14)#
           , (14,13), (14,4), (14,15), (15,14), (15,4), (15,16), (16,15)#
           , (16,4), (16,17), (17,16), (17,4), (17,5), (17,6), (17,18)#
           , (18,17), (18,6), (18,19), (19,18), (19,6), (19,20), (20, 19)#
           , (20,6), (20,21), (21,20), (21,6), (21,7), (21,8), (21,22)#
           , (22,21), (22,8), (22,23), (23,22), (23,8), (23,24), (24,23)#
           , (24,8), (24,9)]

nombresNodos = ["Plaza Moreno", "Plaza San Matín", "Plaza Dardo Rocha", "Plaza Máximo Paz"
                , "Plaza Hipólito Yrigoyen", "Plaza Malvinas Argentinas", "Plaza Azcuénaga"
                , "Plaza Paso", "Plaza Italia", "Plaza Rivadavia", "Fiscalía del Estado"
                , "Plaza Matheu", "Plaza España", "Plaza Saavedra", "Plaza Sarmiento"
                , "Plaza Castelli", "Plaza Brandsen", "Plaza Vucetich", "Plaza 19 de noviembre"
                , "Plaza Alberti", "Plaza Güemes", "Plaza Belgrano", "Plaza Olazábal", "Plaza Alsina"
                , "Dirección de Migraciones" ]

pesos = [8, 5, 5, 7, 4, 9, 4, 9, 4, 7, 9, 8, 6, 8, 4, 6, 
         6, 6, 6, 7, 3, 5, 7, 4, 2, 5, 3, 5, 4, 7, 4, 4,
        3, 4, 3, 3, 4, 2, 5, 4, 6, 4, 5, 4, 3, 3, 4, 8,
        8, 3, 4, 6, 10, 6, 8, 5, 5, 8, 7, 5, 3, 3, 4, 6,
        3, 4, 3, 4, 4, 2, 6, 4, 6, 4, 5, 2, 3, 2, 5, 3, 
        2, 3, 4, 4, 6, 4, 5, 3, 5, 3, 3, 4, 5, 3, 2, 3,
        6, 4, 6, 4, 5, 4, 4, 2, 3, 5, 5, 7, 2, 4, 6]

grafoRutaTamal = ig.Graph()

grafoRutaTamal.add_vertices(25)
grafoRutaTamal.add_edges(edgelist)

grafoRutaTamal.vs["label"] = nombresNodos
grafoRutaTamal.es["weight"] = pesos

def mostrar_menu():
    print("=== Bienvenido a La Ruta del Tamal ===")
    print("Por favor, seleccione su ubicación para recibir el pedido:")
    for i in range(grafoRutaTamal.vcount()):
        print(f"{i+1}. {grafoRutaTamal.vs[i]["label"]}")
    print("0. Salir")

def obtener_ruta(nodo):
    shortest_path = grafoRutaTamal.get_shortest_paths(0, nodo, weights='weight')
    path_indices = shortest_path[0]
    path_labels = [grafoRutaTamal.vs[i]["label"] for i in path_indices]
    print(f"\nPedido recibido para " + grafoRutaTamal.vs[nodo]["label"])
    print("Enviando domiciliario por la siguiente ruta:")
    print("Ruta más corta:", " -> ".join(path_labels))
    print("Pedido en camino...\n")

def agregar_nodo():
    nodo = grafoRutaTamal.add_vertices(1)
    grafoRutaTamal.vs[grafoRutaTamal.vcount() - 1]["label"] = input("Escriba el nombre del nuevo punto de entrega: ")

def recibir_pedido():
    while True:
        print("Seleccione la opción que desee:")
        print("1. Agregar lugar de entrega")
        print("2. Hacer un pedido")
        print("3. Mostrar cantidad de lugares de entrega")
        print("4. Salir")
        control = int(input("Ingrese el número de la opción: "))
        if control == 1:
            agregar_nodo()
        elif control == 2:
            while True:
                mostrar_menu()
                opcion = int(input("Ingrese el número de su ubicación: "))

                if opcion == 0:
                    print("¡Gracias por usar La Ruta del Tamal!")
                    break
                try:
                    nodo = opcion -1
                    ruta = obtener_ruta(nodo)
                    break
                except (IndexError, ValueError):
                    print("Opción inválida. Intente nuevamente.\n")
        elif control == 3:
            print(f"\nActualmente hay {grafoRutaTamal.vcount()} lugares de entrega registrados.\n")
        elif control == 4:
            print("Gracias por usar nuestros servicios.")
            break
        else:
            print("Esa opción no está disponible. Intente nuevamente.")

recibir_pedido()