from collections import deque

# Definir el laberinto
maze = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Definir la posición inicial del jugador y la posición de la salida
start = (0, 0)
end = (5, 5)

# Definir las direcciones en las que el jugador puede moverse
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Definir la función BFS para encontrar la salida más cercana
def bfs(maze, start, end):
    # Inicializar la cola y agregar la posición inicial del jugador
    queue = deque([start])
    # Inicializar un conjunto para almacenar los nodos visitados
    visited = set([start])

    # Inicializar un diccionario para almacenar los nodos y sus distancias desde el nodo inicial
    distances = {start: 0}

    while queue:
        # Sacar el primer nodo de la cola
        current_node = queue.popleft()

        # Si el nodo actual es la salida, devolver la distancia
        if current_node == end:
            return distances[current_node]

        # Explorar todos los nodos vecinos
        for direction in directions:
            x = current_node[0] + direction[0]
            y = current_node[1] + direction[1]

            # Verificar que el nodo vecino esté dentro del laberinto y no sea una pared
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                # Verificar si el nodo vecino ya ha sido visitado
                if (x, y) not in visited:
                    # Agregar el nodo vecino a la cola y al conjunto de nodos visitados
                    queue.append((x, y))
                    visited.add((x, y))

                    # Actualizar la distancia del nodo vecino desde el nodo inicial
                    distances[(x, y)] = distances[current_node] + 1

    # Si no se encuentra la salida, devolver -1
    return -1

# Llamar a la función BFS y mostrar la salida más cercana
distance = bfs(maze, start, end)
print("La salida más cercana está a una distancia de:", distance)