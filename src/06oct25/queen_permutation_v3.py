def queen_permutations(n):
    def backtrack(row, columns, diag1, diag2):
        """
        один шаг подсчета расстановок
        :param row: номер ряда, на котором мы фокусируемся
        :param columns: занятые колнки в двоичном числе. 0 - свободно, 1 - занято
        :param diag1: двоичное число диагонали в обозначении ряд + колнка
        :param diag2: двоичное число диагонали ряд - колонка
        :return: количество расстановок с текущего ряда
        """
        if row == n:
            return 1
        count = 0
        # число, обозначающее занятые позиции. в начале это n единиц
        all_positions = (1 << n) - 1
        # объединяем все недоступные поля (которые биты двоичного числа)
        attacked = columns | diag1 | diag2
        # убираем из всех единиц недоступные и получаем доступные поля
        available = all_positions & ~attacked
        # выбираем свободные позиции пока такие есть
        while available:
            # самый правый в свободных бит (- меняет все 1 на 0 и дабавляет 1)
            cell = available & -available
            # убираем его из свободных
            available -= cell
            # ищем расстановки с уже занятой этой клеткой для следующего ряда
            count += backtrack(row + 1, columns | cell, (diag1 | cell) << 1, (diag2 | cell) >> 1)
        return count
    # вначале доска пустая
    return backtrack(0, 0, 0, 0)

if __name__ == "__main__":
    print(queen_permutations(7))