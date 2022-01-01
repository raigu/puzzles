import math
import re


def possibilities(n):
    c = [0] * n

    overflow = False
    while not overflow:
        i = 0
        while i < n:
            c[i] += 1
            if c[i] > 100:
                c[i] = 0
                i += 1
            else:
                break
        if i < n:
            if sum(c) == 100 and 0 not in c:
                yield c
        else:
            overflow = True


if __name__ == '__main__':
    with open('input') as f:
        ingredients = []
        for l in f.readlines():
            m = re.search(
                r'(\w+): capacity ([-\d]+), durability ([-\d]+), flavor ([-\d]+), texture ([-\d]+), calories (\d+)',
                l.strip())
            ingredients.append([
                m.group(1),
                int(m.group(2)),
                int(m.group(3)),
                int(m.group(4)),
                int(m.group(5)),
                int(m.group(6))
            ])

properties = []  # row - property, col - ingredient
for p in range(len(ingredients[0]) - 1):
    row = []
    for i in ingredients:
        row.append(i[p + 1])
    properties.append(row)

teaspoons = 100
cookies = [0] * len(ingredients)

answer1 = 0
answer2 = 0

for cookies in possibilities(len(ingredients)):
    scores = [0] * len(ingredients[0][1:-1])
    calories = 0
    for i, ingredient in enumerate(ingredients):
        for p, score in enumerate(ingredient[1:-1]):
            scores[p] += cookies[i]*score
        calories += ingredient[-1]*cookies[i]
    for i in range(len(scores)):
        if scores[i] < 0:
            scores[i] = 0

    if math.prod(scores) > answer1:
        answer1 = math.prod(scores)

    if calories == 500 and math.prod(scores) > answer2:
        answer2 = math.prod(scores)


# 225000000 - too high
# 190411776 - too high
print('Part1: ', answer1)
print('Part2: ', answer2)