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