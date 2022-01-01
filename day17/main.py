from copy import copy

ID = 0
CAPACITY = 1

variants = set()

def variants_count(inventory, reminder, path) -> int:
    if reminder == 0:
        path = list(path)
        sorted(path)
        key = ','.join(path)
        if key in variants:
            return 0
        else:
            

    ret = 0
    for i in range(len(inventory)):
        next_inventory = list(inventory)
        container = next_inventory.pop(i)
        if reminder - container[CAPACITY] >= 0:
            next_path = copy(path)
            next_path.add(container[ID])
            ret += variants_count(next_inventory, reminder - container[CAPACITY])
    return ret


if __name__ == '__main__':
    version = 1

    if version == 1:
        file = 'input1'
        liters = 25
    else:
        file = 'input'
        liters = 150

    inventory = []
    with open(file) as f:
        id = 1
        for l in f.readlines():
            capacity = int(l.strip())
            inventory.append((id, capacity))
            id += 1

    print('Part 1:', variants_count(inventory, liters, set()))
