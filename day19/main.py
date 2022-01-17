from collections import defaultdict


def part1(molecule, replacements):
    variants = set()

    i = 0
    while i < len(molecule):
        j = i + 1
        while j <= len(molecule):
            if molecule[i:j] in replacements:
                for r in replacements[molecule[i:j]]:
                    variants.add(molecule[0:i] + r + molecule[j:])
            j += 1
        i += 1

    return len(variants)


if __name__ == '__main__':

    replacements = defaultdict(list)
    with open('input') as f:
        lines = f.read().split("\n")
        i = 0

        while lines[i] != '':
            (f, t) = lines[i].split(' => ')
            replacements[f].append(t)
            i += 1

        molecule = lines[i+1]

    # 195 was too low
    print('Part1: ', part1(molecule, replacements))
