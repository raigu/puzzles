

def houses(directions):
    """
    >>> houses(">")
    2
    >>> houses("^>v<")
    4
    >>> houses("^v^v^v^v^v")
    2
    """

    map = {
        '^': [0, 1],
        '>': [1, 0],
        'v': [0, -1],
        '<': [-1, 0],
    }

    def key(point):
        return f'{point[0]},{point[1]}'

    current = [0,0]
    visited1 = {}
    visited2 = {}
    visited1[key(current)] = 1
    visited2[key(current)] = 2

    santa = True
    current_santa = [0,0]
    current_robo = [0,0]
    for c in directions:
        step = map[c]
        current = [current[0] + step[0], current[1] + step[1]]
        k = key(current)
        if k not in visited1:
            visited1[k] = 0
        visited1[k] += 1

        if santa:
            current_santa = [current_santa[0] + step[0], current_santa[1] + step[1]]
            current2 = current_santa
        else:
            current_robo =  [current_robo[0] + step[0], current_robo[1] + step[1]]
            current2 = current_robo

        santa = not santa

        k = key(current2)
        if k not in visited2:
            visited2[k] = 0
        visited2[k] += 1

    return len(visited1), len(visited2)

if __name__ == '__main__':
    with open('input') as f:
        line = f.readline()

    print(houses(line.strip()))