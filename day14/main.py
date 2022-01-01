import re


def part1(v, t1, t2, t):
    """
    >>> part1(14, 10, 127, 10)
    140
    >>> part1(10,2,1,6)
    40
    >>> part1(1,1,1,2)
    1
    >>> part1(1,1,1,1)
    1
    >>> part1(14, 10, 127, 1000)
    1120
    >>> part1(16,11,162,1000)
    1056
    """
    ret = (t // (t1+t2))*(v*t1)
    r = t % (t1 + t2)
    if r > t1:
        r = t1
    ret += r*v
    return ret



#file = 'input1';duration = 1000;
file = 'input'; duration = 2503;

answer = 0
with open(file) as f:
    for l in f.readlines():
        m = re.search('(?P<dear>\w+) can fly (?P<v>\d+) km/s for (?P<t1>\d+) seconds, but then must rest for (?P<t2>\d+) seconds.', l.strip())

        d = part1(
            int(m.group('v')),
            int(m.group('t1')),
            int(m.group('t2')),
            duration
        )
        if d > answer:
            answer = d

print(answer)


# part2


answer = 0
deers = []
with open(file) as f:
    for l in f.readlines():
        m = re.search('(?P<dear>\w+) can fly (?P<v>\d+) km/s for (?P<t1>\d+) seconds, but then must rest for (?P<t2>\d+) seconds.', l.strip())
        deers.append([
            0, # distance
            0, # points
            int(m.group('v')),
            int(m.group('t1')),
            int(m.group('t2'))
        ])

for s in range(duration):
    lead = 0
    for i, [d, p, v, t1, t2] in enumerate(deers):
        r = (s % (t1+t2))+1
        if r <= t1:
            deers[i][0] += v
        if deers[i][0] > lead:
            lead = deers[i][0]

    for i, [d, p, v, t1, t2] in enumerate(deers):
        if d == lead:
            deers[i][1] += 1


answer = max([d[1] for d in deers])

# 622 <- too low
# 2296 <- too high
print(answer)
