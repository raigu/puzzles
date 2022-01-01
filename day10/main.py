
sequence = '3113322113'
for i in range(50):
    c = 0
    j = 0
    next = ''
    while j < len(sequence):
        k = 1
        while (j+k < len(sequence) and sequence[j] == sequence[j+k]):
            k += 1
        next += str(k) + sequence[j]
        j += k


    sequence = next

    if i == 39:
        print('Part1 ', len(sequence))

print('Part2 ', len(sequence))