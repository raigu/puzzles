


if __name__ == "__main__":

    with open('input') as f:
        line = f.readline()

    floor = 0
    part2 = None
    for p, c in enumerate(line):
        if c == '(':
            floor += 1
        else:
            if floor == 0 and part2 is None:
                part2 = p

            floor -= 1

    print(floor)
    print(part2+1)
