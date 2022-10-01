"""Дополнительный модуль: обработка игрового процесса."""
from typing import Set, Any


def show_field(turns) -> str:
    board = ''
    for i in range(len(turns)):
        for j in range(len(turns)):
            last_char = '' if j == len(turns) - 1 else '|'
            if turns[i][j] == 0:
                board += '   '
            elif turns[i][j] % 2 == 0:
                board += ' O '
            else:
                board += ' X '
            board += last_char
        if i < len(turns) - 1:
            board += ('\n' + '-' * 11 + '\n')

    return board


def wins(x):
    res = set()
    res_list = [i % 2 != 0 for i in x if i != 0]
    if len(res_list) == 3:
        res = set(res_list)
    return res


def check_win(turns) -> set[bool | Any] | set[Any]:
    global win_columns
    columns = [[turns[j][i] for j in range(len(turns))] for i in range(len(turns))]
    diagonals = ([turns[0][0], turns[1][1], turns[2][2]], [turns[0][2], turns[1][1], turns[2][0]])

    for i in range(len(turns)):
        win_rows = wins(turns[i])
        if len(win_rows) == 1:
            return win_rows

    for i in range(len(columns)):
        win_columns = wins(columns[i])
        if len(win_columns) == 1:
            return win_columns

    for i in range(len(diagonals)):
        win_diagonals = wins(diagonals[i])
        if len(win_columns) == 1:
            return win_diagonals


move = [[0, 4, 1],
        [0, 2, 3],
        [0, 0, 5]]

print(show_field(move))
print(*check_win(move))

