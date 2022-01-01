
def rule1(aunt) -> bool:
    r = dict(
        children=3,
        samoyeds=2,
        akitas=0,
        vizslas=0,
        cars=2,
        perfumes=1,
        trees=3,
        cats=7,
        goldfish=5,
        pomeranians=3,
    )

    for n, v in aunt.items():
        if n in r and v != r[n]:
            return False

    return True


def rule2(aunt) -> bool:
    r = dict(
        children=3,
        samoyeds=2,
        akitas=0,
        vizslas=0,
        cars=2,
        perfumes=1,
    )

    greater = dict(
        trees=3,
        cats=7,
    )

    lesser = dict(
        goldfish=5,
        pomeranians=3,
    )

    for n, v in aunt.items():
        if n in r and v != r[n]:
            return False

        if n in greater and v <= greater[n]:
            return False

        if n in lesser and v >= lesser[n]:
            return False

    return True


with open('input') as f:
    i = 1
    for l in f.readlines():
        aunt = {}
        a, p = l.strip().split(":", maxsplit=1)
        for k in p.split(","):
            n, v = k.split(": ")
            aunt[n.strip()] = int(v)

        if rule1(aunt):
            print('Part 1: ', i)

        if rule2(aunt):
            print('Part 2: ', i)
        i += 1
