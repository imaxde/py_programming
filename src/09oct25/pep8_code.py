def count_queen_arrangements(board_size: int) -> int:
    """
    Возвращает количество возможных расстановок N ферзей на шахматной доске размером NxN,
    при которых ферзи не атакуют друг друга
    """

    def place_queen(row_index: int, board_state: list[int]) -> int:
        """
        Рекурсивно пробует расставить ферзей по строкам.
        Возвращает количество корректных вариантов для текущего состояния доски
        """
        # Базовый случай: если все строки заняты, найдено одно корректное решение
        if row_index == board_size:
            return 1
        count = 0
        # Перебираем возможные позиции в текущей строке
        for column_index in range(board_size):
            correct = True
            # Проверяем, не конфликтует ли новая позиция с ранее поставленными ферзями
            for prev_row in range(row_index):
                if (board_state[prev_row] == column_index or
                    board_state[prev_row] + prev_row == column_index + row_index or
                    board_state[prev_row] + prev_row == column_index + row_index):
                    correct = False
                    break
            # Если все нормально, пробуем поставить ферзя и продолжаем рекурсию
            if correct:
                board_state[row_index] = column_index
                count += place_queen(row_index + 1, board_state)
        return count

    # Создание пустой доски
    initial_board = [-1] * board_size
    return place_queen(0, initial_board)


if __name__ == "__main__":
    print(count_queen_arrangements(7))
