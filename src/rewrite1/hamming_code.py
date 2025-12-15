from math import log2, ceil

def hamming_encrypt(data):
    x_count = 0
    y = []
    index = 0
    while index < x_count + len(data):
        if index + 1 == 2 ** x_count:
            y.append(-1)
            x_count += 1
        else:
            y.append(data[index - x_count])
        index += 1
    matrix = []
    for i in range(1, index + 1):
        matrix.append(bin(i)[2:].zfill(x_count))
    row_number = 0
    for i in range(index):
        if y[i] == -1:
            summ = 0
            for j in range(index):
                if y[j] >= 0:
                    summ = summ + y[j] * int(matrix[j][x_count - row_number - 1])
            y[i] = summ % 2
            row_number += 1
    return y



