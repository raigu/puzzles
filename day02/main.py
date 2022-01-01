def wrapping_paper(l, w, h) -> int:
    """
    >>> wrapping_paper(2,3,4)
    58
    >>> wrapping_paper(1,1,10)
    43
    """

    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def ribbon(l, w, h) -> int:
    """
    >>> ribbon(2,3,4)
    34
    >>> ribbon(1,1,10)
    14
    """
    a = [l, w, h]
    a.sort()

    return 2 * a[0] + 2 * a[1] +  a[0] * a[1] * a[2]


if __name__ == '__main__':
    part1 = 0
    part2 = 0
    with open('input') as f:
        for line in f.readlines():
            args = line.strip().split('x')
            args = list(map(int, args))

            part1 += wrapping_paper(*args)
            part2 += ribbon(*args)

    print(part1)
    print(part2)
