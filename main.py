
def solver(sudoku):
    if not is_cell_empty(sudoku):
        return True

    row, col = is_cell_empty(sudoku)

    for number in range(1,10):
        if is_valid(sudoku, row, col, number):
            sudoku[row][col] = number

            if solver(sudoku):
                return True

            sudoku[row][col] = 0

    return False


def is_cell_empty(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col

    return None


def is_valid(sudoku, row, col, number):
    #Check rows
    if number in sudoku[row]:
        return False

    #Check columns
    if number in [sudoku[r][col] for r in range(9)]:
        return False

    #Check boxes
    start_row = row - row % 3
    start_col = col - col % 3
    if number in [
        sudoku[r][c]
        for r in range(start_row, start_row + 3)
        for c in range(start_col, start_col + 3)
    ]:
        return False

    return True


if __name__ == "__main__":
    sudoku = [
        [5, 0, 0, 0, 0, 0, 0, 8, 1],
        [0, 1, 0, 0, 8, 7, 0, 6, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 0, 6, 1, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 4, 0],
        [9, 0, 0, 0, 4, 8, 7, 0, 0],
        [0, 8, 0, 3, 0, 0, 0, 0, 0]
    ]
    if solver(sudoku):
        for s in sudoku:
            print(s)
    else:
        print('No solution')
