def wire_value(wire: str, c: dict) -> int:
    if wire.isnumeric():
        return int(wire)

    expr = c[wire]
    if isinstance(expr, int):
        return expr

    parts = expr.split(' ')
    if parts[0] == 'NOT':
        value = ~ wire_value(parts[1], c) & (pow(2, 16) - 1)
    elif parts[1] == 'AND':
        value = wire_value(parts[0], c) & wire_value(parts[2], c)
    elif parts[1] == 'OR':
        value = wire_value(parts[0], c) | wire_value(parts[2], c)
    elif parts[1] == 'RSHIFT':
        value = wire_value(parts[0], c) >> wire_value(parts[2], c)
    elif parts[1] == 'LSHIFT':
        value = wire_value(parts[0], c) << wire_value(parts[2], c)
    elif parts[1] == '->':
        value = wire_value(parts[0], c)
    else:
        raise Exception('Could not parse expression. ' + expr)

    c[wire] = value

    return value


if __name__ == '__main__':

    with open('input') as f:
        circuit = {}
        for line in f.readlines():
            parts = line.strip().rsplit(' ', 1)
            circuit[parts[1]] = parts[0]

    old = circuit.copy()

    a = wire_value('a', circuit)
    print('Part1: ', a)

    old['b'] = a
    a = wire_value('a', old)
    print('Part2: ', a)
