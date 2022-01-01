def calc(line: str) -> int:
    """
    >>> calc(r'"\\x27"')
    1
    >>> calc(r'"aaa\"aaa"')
    7
    >>> calc('""')
    0
    >>> calc('"abc"')
    3
    """
    i = 0
    line = line[1:-1]
    r = 0
    while i < len(line):
        if line[i] == '\\':
            if line[i + 1] == 'x':
                i += 3
            else:
                i += 1
        i += 1
        r += 1
    return r


def eee(line: str) -> str:
    """
    >>> len(eee('""'))
    6
    """
    ret = ''
    for i in line:
        if i == '"':
            ret += '\\"'
        elif i == '\\':
            ret += '\\\\'
        else:
            ret += i

    return '"' + ret + '"'


if __name__ == '__main__':
    with open('input') as f:
        m = 0
        c = 0
        c2 = 0
        for line in f.readlines():
            line = line.strip()
            c += len(line)
            c2 += len(eee(line))
            m += calc(line)

    print(m, c, c2)

    print('Part1: ', c - m)
    print('Part2: ', c2 - c)
