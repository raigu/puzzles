import sys
from collections import defaultdict
from itertools import permutations

with open('input') as f:

    cities = set()
    distances = defaultdict(dict)

    for line in f.readlines():
        parts = line.strip().split(' ')
        distances[parts[0]][parts[2]] = int(parts[4])
        distances[parts[2]][parts[0]] = int(parts[4])

        cities.add(parts[0])
        cities.add(parts[2])

    min = sys.maxsize
    max = 0
    for variant in permutations(cities):
        distance = 0
        for i in range(len(variant)-1):
            distance += distances[variant[i]][variant[i+1]]

        if distance < min:
            min = distance

        if distance > max:
            max = distance

    print('Part1 ', min)
    print('Part2 ', max)




