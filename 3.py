import random

# Definir el conjunto de caracteres permitidos
CHARACTER_SET = "0123456789"

# Definir el tamaño de la contraseña
PASSWORD_LENGTH = 9

# Definir las teclas adyacentes
ADJACENT_KEYS = {
    "0": ["8"],
    "1": ["2", "4"],
    "2": ["1", "3", "5"],
    "3": ["2", "6"],
    "4": ["1", "5", "7"],
    "5": ["2", "4", "6", "8"],
    "6": ["3", "5", "9"],
    "7": ["4", "8"],
    "8": ["0", "5", "7", "9"],
    "9": ["6", "8"],
}

# Definir las secuencias deseadas y no deseadas
DESIRED_SEQUENCES = [[1, 9, 4, 6, 3, 7, 5], [9, 1, 3, 7, 2, 8, 5]]
UNDESIRED_SEQUENCES = [[1, 2, 3, 4, 5, 6, 9, 8, 7], [1, 2, 5, 3, 6, 9, 8, 7, 4]]

def generate_random_password():
    """Generar una contraseña aleatoria"""
    return "".join(random.choice(CHARACTER_SET) for _ in range(PASSWORD_LENGTH))

def calculate_fitness(password):
    """Calcular la aptitud de una contraseña basada en la máxima distancia entre teclas y las secuencias deseadas y no deseadas"""
    fitness = 0
    for i in range(PASSWORD_LENGTH - 1):
        if password[i+1] in ADJACENT_KEYS[password[i]]:
            fitness -= 1
        if [int(password[i]), int(password[i+1])] in UNDESIRED_SEQUENCES:
            fitness -= 2
        if [int(password[i]), int(password[i+1])] in DESIRED_SEQUENCES:
            fitness += 2
    return fitness

def crossover(parent1, parent2):
    """Realizar el cruce de dos padres para generar un hijo"""
    crossover_point = random.randint(1, PASSWORD_LENGTH - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutation(password):
    """Realizar una mutación en una contraseña"""
    mutation_point = random.randint(0, PASSWORD_LENGTH - 1)
    mutated_character = random.choice(CHARACTER_SET.replace(password[mutation_point], ""))
    password = password[:mutation_point] + mutated_character + password[mutation_point+1:]
    return password

def genetic_algorithm():
    """Algoritmo genético para generar contraseñas"""
    population_size = 100
    generations = 50
    mutation_rate = 0.1

    # Generar una población inicial de contraseñas aleatorias
    population = [generate_random_password() for _ in range(population_size)]

    for generation in range(generations):
        # Calcular la aptitud de la población
        fitness_scores = [calculate_fitness(password) for password in population]

        # Seleccionar los mejores padres para el cruce
        parents = random.sample(population, 2)

        # Realizar el cruce y la mutación para generar una nueva población
        offspring = crossover(parents[0], parents[1])
        if random.random() < mutation_rate:
            offspring = mutation(offspring)

        # Reemplazar a un miembro aleatorio de la población con el nuevo individuo
        population[random.randint(0, population_size - 1)] = offspring

    # Devolver la contraseña con mayor aptitud como resultado
    best_password = max(population, key=calculate_fitness)
    return best_password

# Ejecutar el algoritmo genético y obtener la contraseña generada
generated_password = genetic_algorithm()
print("Contraseña generada:", generated_password)