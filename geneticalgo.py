"""
    Name : Abdul Aziz Muhammad Ibrahim Isa
    Roll No: P17-6143
    Ai Assignment # 2
    Traveling salesman problem with Genetic Alforithms.
"""
import random
import copy
TSP = [[0,66,21,300,500,26,77,69,125,650],
        [66, 0, 35, 115, 36, 65, 85, 90, 44, 54],
        [21, 35, 0, 450, 448, 846, 910, 47, 11, 145],
        [300, 115, 450, 0, 65, 478, 432, 214, 356, 251],
        [500, 36, 448, 65, 0, 258, 143, 325, 125, 39],
        [26, 65, 846, 478, 258, 0, 369, 256, 345, 110],
        [77, 85, 910, 432, 143, 369, 0, 45, 120, 289],
        [69, 90, 47, 214, 325, 256, 45, 0, 325, 981],
        [125, 44, 11, 356, 125, 345, 120, 325, 0, 326],
        [650, 54, 145, 251, 39, 110, 289, 981, 326, 0]]
shortest_path = ""
shortest_distance = 10000

def distance(population, type):
    dists = []
    distx = []
    global shortest_distance
    global shortest_path
    for chromosomes in population:
        dist = 0
        for i in range(0, len(chromosomes)):
            if i != len(chromosomes)-1:
                dist += TSP[chromosomes[i]][chromosomes[i+1]]
            else:
                dist += TSP[chromosomes[i]][chromosomes[0]]
        if(shortest_distance > dist):
            shortest_distance = dist
            shortest_path = ""
            for i in chromosomes:
                shortest_path += str(i) + "->"
            shortest_path += str(chromosomes[0])
        dists.append(dist)
        distx.append((dist, chromosomes))
    if(type == 0):
        return dists
    else:
        return distx
def crossover(parent):
    parent1 = parent[0]
    parent2 = parent[1]

    cross1 = parent1[-3:]
    cross2 = parent2[-3:]
    for i in cross1:
        if i in parent2:
            parent2.remove(i)
    random.shuffle(cross1)
    for i in cross1:
        parent2.append(i)

    for i in cross2:
        if i in parent1:
            parent1.remove(i)
    random.shuffle(cross2)
    for i in cross2:
        parent1.append(i)
    return [parent1, parent2]
def mutation(childrens):
    for i in range(0, len(childrens)):
        x = random.sample(range(0, 10), 4)
        childrens[i][x[0]],childrens[i][x[1]] = childrens[i][x[1]],childrens[i][x[0]]
        #childrens[i][x[2]],childrens[i][x[3]] = childrens[i][x[3]],childrens[i][x[2]]
    return childrens
def genetics():
    # make initial population
    population = []
    minu = []
    for i in range(0, 40):
        temp = random.sample(range(0, 10), 10)
        population.append(temp)
    iteration = 0
    while(iteration < 30000):
        #calculate fitness value of population
        prob = distance(population, 0)
        sum = 0
        for i in range(0, len(prob)):
            sum += prob[i]
        for i in range(0, len(prob)):
            prob[i] = prob[i] / sum
            prob[i] = 1 - prob[i]
        # apply crossover and make childrens
        children = []
        for i in range(0, int(len(population)/2)):
            parent = random.choices(population, prob, k=2)
            childs = crossover(parent)
            children.append(childs[0])
            children.append(childs[1])
        # appling mutation to children
        children = mutation(children)
        #combining parents with children
        for childs in children:
            population.append(childs)
        #calculate fitness value and discard half the population
        fitness = distance(population, 1)
        for i in range(0, int(len(fitness)/2)):
            fitness.remove(max(fitness))
        iteration = iteration + 1
        population = []
        for tuples in fitness:
            population.append(tuples[1])
        print("shortest distance => ", shortest_distance, "shortest_path => ", shortest_path, "generation => ", iteration)


genetics()
