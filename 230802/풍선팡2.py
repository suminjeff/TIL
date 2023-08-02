import sys
sys.stdin = open("input.txt", "r")


def my_max(num_list):
    max_v = 0
    for num in num_list:
        if max_v < num:
            max_v = num
    return max_v


T = int(input())
for tc in range(1, T+1):
    row, col = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]

    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    result_list = []

    for r in range(row):
        for c in range(col):
            flower = arr[r][c]
            for d in range(4):
                pop_r = r + d_row[d]
                pop_c = c + d_col[d]
                if 0 <= pop_r < row and 0 <= pop_c < col:
                    flower += arr[pop_r][pop_c]
                result_list.append(flower)

    print(f"#{tc} {my_max(result_list)}")
