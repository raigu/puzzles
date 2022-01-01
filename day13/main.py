import re
import sys
from itertools import permutations

with open('input') as f:
    lines = f.readlines()
pattern = r'^(?P<person1>\w+) would (?P<op>\w+) (?P<points>\d+) happiness units by sitting next to (?P<person2>\w+).$'

persons = set()
for l in lines:
    m = re.search(pattern, l)
    persons.add(m.group('person1'))
    persons.add(m.group('person2'))

persons = list(persons) # change to list so every person will have an index.
happiness = [[0]*len(persons) for _ in range(len(persons))]
for l in lines:
    m = re.search(pattern, l)
    p1 = m.group('person1')
    p2 = m.group('person2')
    happiness[persons.index(p1)][persons.index(p2)] = (1 if m.group('op') == 'gain' else -1) * int(m.group('points'))

answer1 = -sys.maxsize
for p in permutations(range(len(persons))):
    c = 0 # total change in happiness
    for i in range(len(p)):
        cur = p[i]
        prev = p[(i-1+len(p))%len(p)]
        next = p[(i+1)%len(p)]
        c += (happiness[cur][prev] + happiness[cur][next])
    if c > answer1:
        answer1 = c

print('Part1 ', answer1)

answer2 = -sys.maxsize
persons.append('Me')

for h in happiness:
    h.append(0)
happiness.append([0]*len(persons))

for p in permutations(range(len(persons))):
    c = 0 # total change in happiness
    for i in range(len(p)):
        cur = p[i]
        prev = p[(i-1+len(p))%len(p)]
        next = p[(i+1)%len(p)]
        c += (happiness[cur][prev] + happiness[cur][next])
    if c > answer2:
        answer2 = c

print('Part2 ', answer2)


