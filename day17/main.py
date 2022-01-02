import sys
from copy import copy


class Container:
    """
    I am a container. I have a capacity. I am immutable and hashable.

    Is hashable
    >>> hash(Container(1, 1)) != 0
    True

    Tuple of containers is hashable
    >>> hash(tuple([Container(1, 1), Container(1, 1)])) != 0
    True

    Two different instances with same capacity must not have same hash
    >>> hash(Container(1, 10)) != hash(Container(2, 10))
    True

    Can be sorted by capacity if in list
    >>> l = [Container(2, 10), Container(1, 5)]; sorted(l)
    [Container(1,5), Container(2,10)]
    """

    last_id = 0

    def __init__(self, id: int, capacity: int) -> None:
        self._id = id
        self._capacity = capacity
        super().__init__()

    @property
    def capacity(self) -> int:
        return self._capacity

    def __eq__(self, other):
        if isinstance(other, Container):
            return other._id == self._id
        raise NotImplemented()

    def __hash__(self) -> int:
        return hash(self._id)

    def __repr__(self) -> str:
        return f'Container({self._id},{self._capacity})'

    def __lt__(self, other):
        """
        If same capacity, orer by id
        >>> sorted([Container(2,5), Container(1,5)])
        [Container(1,5), Container(2,5)]
        """
        if self._capacity == other._capacity:
            return self._id < other._id
        else:
            return self._capacity < other._capacity


variants = set()

def cache_variants_count(func):
    cache = []

    def wrapper(inventory, reminder, path):
        inventory = sorted(inventory)
        path = sorted(path)
        key = tuple([inventory, reminder, path])
        if key not in cache:
            func(inventory, reminder, path)
            cache.append(key)

    return wrapper


def variants_count(inventory, reminder, path) -> None:
    if reminder == 0:
        path = list(path)
        path = sorted(path)
        path = tuple(path) # make hashable
        if path not in variants:
            variants.add(path)
            #print(",".join([f'{i.capacity}({i._id})' for i in path]))
    else:
        for i in range(len(inventory)):
            next_inventory = list(inventory)
            container = next_inventory.pop(i)
            if reminder - container.capacity >= 0:
                next_path = copy(path)
                next_path.add(container)
                variants_count(next_inventory, reminder - container.capacity, next_path)


if __name__ == '__main__':
    version = 0

    if version == 1:
        file = 'input1'
        liters = 25
    else:
        file = 'input'
        liters = 150

    inventory = []
    with open(file) as f:
        for i, l in enumerate(f.readlines()):
            capacity = int(l.strip())
            inventory.append(Container(i, capacity))
    inventory = sorted(inventory)
    cache_variants_count(variants_count(inventory, liters, set()))
    #variants_count(inventory, liters, set())
    # 2341 -- too high
    print('Part 1:', len(variants))

    m = sys.maxsize
    for v in variants:
        if m > len(v):
            m = len(v)

    print('Minimum:', m)
    variants = [v for v in variants if len(v) == m]

    print('Part2:', len(variants))
