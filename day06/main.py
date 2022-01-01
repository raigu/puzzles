

def rectangle(x1, y1, x2, y2) -> list:
    """
    >>> rectangle(0,0,1,0)
    [[0, 0], [1, 0]]
    >>> rectangle(0,0,0,1)
    [[0, 0], [0, 1]]
    >>> rectangle(0,0,2,2)
    [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    """

    if x2 < x1 or y2 < y1:
        raise Exception(x1,y1,x2,y2)


    points = []
    for x in range(x2 - x1 + 1):
        for y in range(y2 - y1 + 1):
            points.append([x1 + x, y1 + y])
    return points


def toggle(grid: set, points: set) -> set:
    """
    >>> toggle({'0,1'},{'0,1'})
    set()
    >>> toggle(set(), {'0,1'})
    {'0,1'}
    """
    on = grid & points
    off = points - on

    grid = grid | off
    grid = grid - on

    return grid

if __name__ == '__main__':

    def key(point):
        return f'{point[0]},{point[1]}'

    """
    # Part 1
    grid = set() # only cells with lights on
    with open('input') as f:
        for line in f.readlines():
            line = line.strip()
            print(line)

            (operation, start, jura, end) = line.rsplit(' ', 3)

            start = list(map(int, start.split(',')))
            end = list(map(int, end.split(',')))

            points = set([key(point) for point in rectangle(start[0], start[1], end[0], end[1])])
            if operation == 'turn on':
                grid = grid | points
            elif operation == 'turn off':
                grid = grid - points
            elif operation == 'toggle':
                grid = toggle(grid, points)


    print(len(grid))
    """

    # Part 2
    grid = {}
    with open('input') as f:
        for line in f.readlines():
            line = line.strip()
            #print(line)

            (operation, start, jura, end) = line.rsplit(' ', 3)

            start = list(map(int, start.split(',')))
            end = list(map(int, end.split(',')))

            points = set([key(point) for point in rectangle(start[0], start[1], end[0], end[1])])
            if operation == 'turn on':
                for point in points:
                    grid[point] = grid.get(point, 0) + 1
            elif operation == 'turn off':
                for point in points:
                    current = grid.get(point, 0)
                    if current > 0:
                        grid[point] = current - 1
            elif operation == 'toggle':
                for point in points:
                    grid[point] = grid.get(point, 0) + 2


    print(sum(grid.values()))