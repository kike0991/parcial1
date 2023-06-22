from collections import deque


# Definimos la clase para representar el laberinto
class Laberinto:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def es_valido(self, fila, columna):
        # Verificamos si las coordenadas están dentro de los límites del laberinto
        if fila >= 0 and fila < self.filas and columna >= 0 and columna < self.columnas:
            # Verificamos si la celda no es un obstáculo
            if self.matriz[fila][columna] != '#':
                return True
        return False

    def encontrar_salida(self, inicio, salida):
        # Definimos las coordenadas de los movimientos posibles (arriba, abajo, izquierda, derecha)
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visitados = set()
        cola = deque([(inicio[0], inicio[1], 0)])  # Usamos una cola para la búsqueda en anchura

        while cola:
            fila, columna, distancia = cola.popleft()

            # Verificamos si hemos llegado a la salida
            if (fila, columna) == salida:
                return distancia

            # Marcamos la celda actual como visitada
            visitados.add((fila, columna))

            # Generamos los movimientos posibles desde la celda actual
            for movimiento in movimientos:
                nueva_fila = fila + movimiento[0]
                nueva_columna = columna + movimiento[1]

                # Verificamos si el movimiento es válido y si la celda no ha sido visitada
                if self.es_valido(nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in visitados:
                    # Agregamos la nueva celda a la cola con la distancia incrementada
                    cola.append((nueva_fila, nueva_columna, distancia +1))

        # Si no se encuentra  salida,  -1
        return -1

# SE REPRESENTA EL LABERINTO COMO UNA MATRIZ,  '#'IGUAL A UN OBSTACULO y '0' A UN ESPACIO LIBRE
laberinto = [
    ['E', '0', '0', '0', '#', '0', '#', '#', '0'],
    ['0', '#', '#', '0', '0', '0', '0', '0', '0'],
    ['0', '#', '0', '0', '#', '0', '0', '#', '#'],
    ['#', '0', '0', '0', '#', '#', '0', '#', '0'],
    ['0', '0', '0', '0', '#', '#', '0', '#', '0'],
    ['0', '#', '#', '0', '0', '#', '0', '0', 'S3'],
    ['0', '#', '0', '0', '0', '0', '0', '0', '#'],
    ['0', '#', '0', '#', '#', '#', '#', '#', '#'],
    ['0', '0', '0', '0', '0', '0', '0', '#', '0'],
    ['#', '0', '0', 'S1', '#', '#', '#', '0', 'S2'],


]

# Creamos una instancia de la clase Laberinto
laberinto_objeto = Laberinto(laberinto)

# se introduce las coordenadas de la salida
inicio = (0, 0)
salida = (9, 6)

# metodo para llamar a la distancia
distancia = laberinto_objeto.encontrar_salida(inicio, salida)

if distancia != -1:
    print(f"La salida está a una distancia de {distancia} pasos.")
else:
    print("No se encontró una salida.")