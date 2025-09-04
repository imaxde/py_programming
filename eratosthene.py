def sieve(top):
    sequence = list(range(2, top + 1))
    focus = 0
    while focus < len(sequence):
        p = sequence[focus]
        for i in range(2 * p, sequence[-1] + 1, p):
            if i in sequence:
                sequence.remove(i)
        focus += 1
    return sequence
