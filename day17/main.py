from copy import copy

ID = 0
CAPACITY = 1

variants = set()

def cache_variants_count(func):
    cache = []

    def wrapper(inventory, reminder, path):
        ids = [str(i[0]) for i in inventory]
        sorted(ids)
        k1 = hash(tuple(ids))
        p = list(path)
        sorted(p)
        k2 = tuple(path)

        key = tuple([hash(k1), reminder, hash(k2)])
        if key not in cache:
            func(inventory, reminder, path)
            cache.append(key)

    return wrapper


def variants_count(inventory, reminder, path) -> None:
    if reminder == 0:
        path = list(path)
        sorted(path)
        key = ','.join([str(p) for p in path])
        if key not in variants:
            variants.add(key)
    else:
        for i in range(len(inventory)):
            next_inventory = list(inventory)
            container = next_inventory.pop(i)
            if reminder - container[CAPACITY] >= 0:
                next_path = copy(path)
                next_path.add(container[ID])
                variants_count(next_inventory, reminder - container[CAPACITY], next_path)


if __name__ == '__main__':
    version = 1

    if version == 2:
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
    cache_variants_count(variants_count(inventory, liters, set()))
    # 2341 -- too high
    print('Part 1:', len(variants))
    print(variants)
