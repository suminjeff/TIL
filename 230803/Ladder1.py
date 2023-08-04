import sys

sys.stdin = open("ladder.txt", "r")


def go_left(arr, r, c):
    for x in range(c, -1, -1):
        if x == 0:
            return 0
        if arr[r][x - 1] == 0:
            return x


def go_right(arr, r, c):
    for x in range(c, 100):
        if x == 99:
            return 99
        if arr[r][x + 1] == 0:
            return x


def find_x(array):
    for x_index in range(100):
        if array[-1][x_index] == 2:
            return x_index


T = 10

for tc in range(1, T + 1):
    t = int(input())
    field = [list(map(int, input().split())) for _ in range(100)]

    col = find_x(field)
    for row in range(99, -1, -1):
        if col == 0 and field[row][col + 1] == 1:
            col = go_right(field, row, col)

        elif col == 99 and field[row][col - 1] == 1:
            col = go_left(field, row, col)

        elif 1 <= col < 99:
            if field[row][col - 1] == 1:
                col = go_left(field, row, col)

            elif field[row][col + 1] == 1:
                col = go_right(field, row, col)

    print(f"#{tc} {col}")
