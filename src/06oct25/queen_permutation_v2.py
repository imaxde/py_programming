def queen_permutations(n):
    def helper(row, board):
        # если все ферзи расставлены найдено корректное решение
        if row == n:
            return 1
        count = 0
        # пробуем поставить ферзя в каждом столбце текущей строки
        for column in range(n):
            correct = True
            # проверка что с новым ферзем все остается нормально
            for i in range(row):
                if board[i] == column or board[i] - i == column - row or board[i] + i == column + row:
                    correct = False
                    break
            if correct:
                board[row] = column
                # добавляем к счетчику все комбинции ферзя со следующего ряда
                count += helper(row + 1, board)
        return count

    # начинаем с первого ряда и пустой доски
    return helper(0, [-1] * n)

print(queen_permutations(7))

