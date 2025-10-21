from itertools import combinations

def check_queen_combination(cell_numbers, n):
    rows = [cell // n for cell in cell_numbers]
    columns = [cell % n for cell in cell_numbers]
    for i in range(1, n):
        for j in range(i):
            # проверяем что не на одной диагонали
            if abs(rows[i] - rows[j]) == abs(columns[i] - columns[j]):
                return False
    if len(set(rows)) != n:
        return False  # если есть свопадающие ряды
    if len(set(columns)) != n:
        return False # если есть совпадающие колонки
    return True

def queen_permutations(n):
    count = 0
    # номера клеток с ферзем слева направо сверху вниз
    for cell_numbers in combinations(range(n * n), n):
        if check_queen_combination(cell_numbers, n):
            count += 1
    return count

if __name__ == "__main__":
    print(queen_permutations(7))