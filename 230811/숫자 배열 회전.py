import sys

sys.stdin = open("숫자 배열 회전.txt", "r")


def turn90(arr):
    turned_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            turned_arr[j][N - 1 - i] = arr[i][j]

    return turned_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    arr_90 = turn90(arr)
    arr_180 = turn90(arr_90)
    arr_270 = turn90(arr_180)

    print(f"#{tc}")

    for i in range(N):
        print("".join(arr_90[i]), end=" ")
        print("".join(arr_180[i]), end=" ")
        print("".join(arr_270[i]), end=" ")
        print()
