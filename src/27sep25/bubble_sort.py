def bubble_sort(iterable):
    length = len(iterable)
    for limit in range(1, length - 1):
        for position in range(length - limit):
            e1, e2 = iterable[position], iterable[position + 1]
            if e1 > e2:
                iterable[position], iterable[position + 1] = e2, e1
    return iterable

bubble_sort([3, 1, 9, 8, 11, 6])
