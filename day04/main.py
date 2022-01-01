import sys
from hashlib import md5


def part1(value):
    """
    >>> part1('abcdef')
    609043
    >>> part1('pqrstuv')
    1048970
    """

    i = 0
    while True:
        m = md5()
        s = f'{value}{i}'
        m.update(s.encode('utf-8'))
        if m.hexdigest()[:5] == '00000':
            return i

        if i == sys.maxsize:
            return -1

        i += 1

if __name__ == '__main__':
    print(part1('yzbqklnj'))