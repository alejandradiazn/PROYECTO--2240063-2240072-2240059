
## **Integrantes del Grupo 2**

 Nombres:                         
**Alejandra Díaz Navarro**  - 2240063     
**Cristián David Quintana** - 2240072    
**Ana María Fernández**     - 2240059    



# **La Ruta del Tamal - Sistema de Entregas Basado en Grafos**

## **Resumen del Problema**

En la ciudad de **La Plata, Argentina**, un grupo de emprendedores colombianos ha inaugurado con éxito un restaurante llamado **"La Ruta del Tamal"**, especializado en tamales tolimenses, santandereanos y vallunos. Debido al rápido crecimiento de los pedidos a domicilio, el equipo decidió implementar un sistema logístico inteligente que optimice las rutas de entrega.

El sistema se basa en un **grafo ponderado no dirigido**, debido al doble sentido presente en las vías del sector, en el cual los nodos representan plazas o puntos clave de entrega, y las aristas representan conexiones directas entre estos puntos, con pesos que indican el tiempo de recorrido en minutos. El nodo central del grafo es **Plaza Moreno**, desde donde parten todas las rutas.

Este desarrollo busca optimizar las entregas domiciliarias calculando el **camino más corto** desde Plaza Moreno hacia cualquier punto de entrega, brindando además la posibilidad de expandir dinámicamente el grafo con nuevas ubicaciones o rutas según las necesidades logísticas.


## **Etapas del Desarrollo**

### 1. **Contextualización y diseño del problema**
- En la primera entrega, se abordó la creación de una estructura de datos dinámica para gestionar rutas de transporte, permitiendo agregar y eliminar paradas.
- En la segunda entrega, esta lógica se adaptó al nuevo contexto de reparto de domicilios en una ciudad, manteniendo la estructura basada en árboles y agregando nuevas funcionalidades logísticas.

### 2. **Implementación del sistema con `igraph`**
- Se construyó el grafo con 25 nodos y sus respectivas conexiones y pesos.
- Se estableció **Plaza Moreno** como centro logístico y nodo raíz del sistema.
- Se asignaron nombres representativos a cada nodo del grafo.

### 3. **Funcionalidades incorporadas**
- **Menú para clientes**: permite solicitar un pedido indicando la plaza de destino y obtiene la ruta más corta desde el nodo central.
- **Menú para empleados** (con contraseña): permite agregar nuevas ubicaciones o trayectos entre nodos.
- Cálculo automático del camino óptimo usando pesos en las aristas.



## **Asignación de Nombres y Nodos**

En la etapa final del desarrollo, se realizó una correspondencia entre letras del alfabeto y ubicaciones reales de la ciudad, asignando posteriormente a cada una un número identificador correspondiente al índice del nodo en el grafo; esto siguiendo la convención previamente asignada por el grupo nen la entrega dos basada en árboles. Por ejemplo:

| Letra | Plaza                                 | Nodo |
|-------|----------------------------------------|------:|
| A     | Plaza Moreno                           | 0     |
| B     | Plaza San Martín                       | 1     |
| C     | Plaza Dardo Rocha                      | 2     |
| D     | Plaza Máximo Paz                       | 3     |
| E     | Plaza Hipólito Yrigoyen                | 4     |
| F     | Plaza Malvinas Argentinas              | 5     |
| G     | Plaza Azcuénaga                        | 6     |
| H     | Plaza Paso                             | 7     |
| I     | Plaza Italia                           | 8     |
| J     | Plaza Rivadavia                        | 9     |
| K     | Fiscalía del Estado                    | 10    |
| L     | Plaza Matheu                           | 11    |
| M     | Plaza España                           | 12    |
| N     | Plaza Saavedra                         | 13    |
| O     | Plaza Sarmiento                        | 14    |
| P     | Plaza Castelli                         | 15    |
| Q     | Plaza Brandsen                         | 16    |
| R     | Plaza Vucetich                         | 17    |
| S     | Plaza 19 de noviembre                  | 18    |
| T     | Plaza Alberti                          | 19    |
| U     | Plaza Güemes                           | 20    |
| V     | Plaza Belgrano                         | 21    |
| W     | Plaza Olazábal                         | 22    |
| X     | Plaza Alsina                           | 23    |
| Y     | Dirección de Migraciones               | 24    |

Esta conversión alfanumérica facilitó tanto la visualización conceptual del sistema como la codificación práctica en la estructura del grafo, permitiendo una asociación clara entre la nomenclatura utilizada en la fase de análisis y la implementación final del código.


## **Requisitos Técnicos**

- Python 3.6
- Librerías necesarias:
  - `igraph`
  - `numpy`

## **Instrucciones de Uso**

1. Ejecuta el script en un entorno Python con las librerías instaladas.
2. Elige entre:
   - **Menú de Cliente** para simular la solicitud de un domicilio.
   - **Menú de Empleado** para modificar el grafo (requiere contraseña: `RutaTamal123`).
3. Sigue las instrucciones en pantalla para realizar pedidos o modificar rutas.


## **Conclusiones Finales**

Este proyecto demuestra el uso práctico de estructuras de datos avanzadas (**grafos ponderados**) para resolver problemas reales de logística urbana. La implementación es flexible y escalable, permitiendo adaptaciones futuras para integraciones con mapas reales, interfaces gráficas o bases de datos.

