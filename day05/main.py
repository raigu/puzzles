

def is_nice(s: str) -> bool:
    """
    >>> is_nice('ugknbfddgicrmopn')
    True
    >>> is_nice('aaa')
    True
    >>> is_nice('jchzalrnumimnmhp')
    False
    >>> is_nice('haegwjzuvuyypxyu')
    False
    >>> is_nice('dvszwmarrgswjxmb')
    False
    """


    wowels = ['a', 'e', 'i', 'o', 'u']
    wc = 0
    for c in s:
        if c in wowels:
           wc += 1
    if wc < 3:
        return False


    twise = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            twise = True

        if f'{s[i]}{s[i+1]}' in ['ab', 'cd', 'pq', 'xy']:
            return False

    if not twise:
        return False

    return True

def is_nice2(s: str) -> bool:
    """
    >>> is_nice2('qjhvhtzxzqqjkmpb')
    True
    >>> is_nice2('xxyxx')
    True
    >>> is_nice2('uurcxstgmygtbstg')
    False
    >>> is_nice2('ieodomkazucvgmuy')
    False
    """

    twise = False
    for i in range(len(s) - 1):
        for j in range(len(s) - 1):
            if f'{s[i]}{s[i+1]}' == f'{s[j]}{s[j+1]}':
                if j < i - 1 or i + 1 < j:
                    twise = True
    if not twise:
        return False

    twise = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            twise = True

    return twise

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    print(sum([is_nice(line.strip()) for line in lines]))
    print(sum([is_nice2(line.strip()) for line in lines]))