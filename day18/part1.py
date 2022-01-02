from itertools import combinations_with_replacement, product

ons = set()

with open('input') as f:
    for y, l in enumerate(f.readlines()):
        for x,c in enumerate(l.strip()):
            if c == '#':
                ons.add((y, x))

steps = 100
max_y = y
max_x = x
print("Size: ", (0, 0), '..', (y, x))
for i in range(steps):
    next = set()
    offs = set()
    for l in ons:
        c = 0
        for d in product([-1,0,1], repeat=2):
            if d == (0, 0):
                continue

            y2 = l[0] + d[0]
            x2 = l[1] + d[1]
            if 0 <= y2 <= max_y and 0 <= x2 <= max_x:
                if (y2, x2) in ons:
                    c += 1
                else:
                    offs.add((y2, x2))
        if 2 <= c <= 3:
            next.add(l)

    for l in offs:
        c = 0
        for d in product([-1, 0, 1], repeat=2):
            if d == (0, 0):
                continue
            y2 = l[0] + d[0]
            x2 = l[1] + d[1]
            if 0 <= y2 <= max_y and 0 <= x2 <= max_x:
                if (y2, x2) in ons:
                    c += 1
        if c == 3:
            next.add(l)

    ons = next

print('Part 1:', len(ons))


