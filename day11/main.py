

def check_rule1(sequence) -> bool:
    """
    >>> check_rule1('hijklmmn')
    True
    """
    k = 0
    while k < len(sequence) - 2:
        if ord(sequence[k]) + 1 == ord(sequence[k + 1]) == ord(sequence[k + 2]) - 1:
            return True
        else:
            k += 1
    return False


def check_rule3(sequence):
    """
    >>> check_rule3('abbceffg')
    True
    >>> check_rule3('abbcegjk')
    False
    """
    k = 0
    one = ' '
    while k < len(sequence) - 1:
        if sequence[k] == sequence[k + 1]:
            if one == ' ':
                one = sequence[k]
            elif one != sequence[k]:
                return True
            k += 1
        k += 1

    return False


def find_next(sequence):
    while True:
        i = 7
        if sequence[i] < 'z':
            sequence[i] = chr(ord(sequence[i]) + 1)
        else:
            sequence[i] = 'a'
            while sequence[i - 1] == 'z':
                sequence[i - 1] = 'a'
                i -= 1

            sequence[i - 1] = chr(ord(sequence[i - 1]) + 1)

        rule1 = check_rule1(sequence)

        rule2 = not ('i' in sequence or 'o' in sequence or 'l' in sequence)

        rule3 = check_rule3(sequence)

        if rule1 and rule2 and rule3:
            break

    return sequence

if __name__ == '__main__':
    sequence = find_next([c for c in 'hepxcrrq'])
    print('Part1 ', ''.join(sequence))



    print('Part2 ', ''.join(find_next(sequence)))