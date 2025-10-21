def heap(collection, index, length):
    head = index
    if index * 2 + 1 < length and collection[head] < collection[index * 2 + 1]:
        head = index * 2 + 1
    if index * 2 + 2 < length and collection[head] < collection[index * 2 + 2]:
        head = index * 2 + 2
    if head != index:
        collection[index], collection[head] = collection[head], collection[index]
        heap(collection, head, length)

def heap_sort(collection):
    n = len(collection)
    for i in range(n // 2, -1, -1):
        heap(collection, i, n)
    for i in range(n - 1, 0, -1):
        collection[i], collection[0] = collection[0], collection[i]
        heap(collection, 0, i)
    return collection
