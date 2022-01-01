import json


def part2(data) -> int:
    """
    >>> part2([1,"red",5])
    6
    >>> part2({"d":"red","e":[1,2,3,4],"f":5})
    0
    >>> part2([1,{"c":"red","b":2},3])
    4
    >>> part2([1,2,3])
    6
    """

    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum([part2(i) for i in data])
    elif isinstance(data, dict):  # object
        ret = 0
        for k, v in data.items():
            if k == 'red':
                return 0
            if v == 'red':
                return 0
            ret += part2(v)
        return ret
    return 0


if __name__ == '__main__':
    with open('input') as f:
        line = f.read()

    i = 0
    part1 = 0
    while i < len(line):
        k = 0
        while line[i + k] == '-' or '0' <= line[i + k] <= '9':
            k += 1
        if k > 0:
            part1 += int(line[i:i + k])

        i += k + 1

    print('Part1', part1)
    print('Part2', part2(json.loads(line)))
