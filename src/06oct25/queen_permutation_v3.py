def queen_permutations(n):
    count = 0
    # текущий ряд, позиции ферзей
    stack = [(0, [])]
    # ряды могут быть только уникальные, поэтому, если все взяли, то все
    while stack:
        row, queens = stack.pop()
        if row == n:
            count += 1
            continue
        # пробуем поставить ферзя в каждую колонку
        for column in range(n):
            # проверяем конфликты
            correct = True
            for r, c in enumerate(queens):
                if c == column or abs(c - column) == abs(r - row):
                    correct = False
                    break
            if correct:
                stack.append((row + 1, queens + [column]))
    return count

print(queen_permutations(7))

