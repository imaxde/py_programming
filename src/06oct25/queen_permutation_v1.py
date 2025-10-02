from itertools import combinations

def queen_permutations(n):
    count = 0
    # номера клеток с ферзем слева направо сверху вниз
    for cell_numbers in combinations(range(n * n), n):
        correct = True
        rows = [cell // n for cell in cell_numbers]
        columns = [cell % n for cell in cell_numbers]
        for i in range(1, n):
            for j in range(i):
                # проверяем что не на одной диагонали
                if abs(rows[i] - rows[j]) == abs(columns[i] - columns[j]):
                    correct = False
                    break
        if not correct:
            continue  # если есть совпадающие диагонали
        if len(set(rows)) != n:
            continue  # если есть свопадающие ряды
        if len(set(columns)) != n:
            continue  # если есть совпадающие колонки
        count += 1
    return count

print(queen_permutations(7))