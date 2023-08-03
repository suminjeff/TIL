import sys

sys.stdin = open("풍선팡.txt", "r")


def my_max(n_list):
    max_v = n_list[0]
    for n in n_list:
        if max_v < n:
            max_v = n
    return max_v


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    delta_row = [0, 0, 1, 0, -1]
    delta_col = [0, 1, 0, -1, 0]

    total_list = []
    for row in range(N):
        for col in range(M):
            total = 0
            for i in range(5):
                dr = row + delta_row[i]
                dc = col + delta_col[i]
                for j in range(1, arr[row][col]+1):
                    if 0 <= dr + j < N and 0 <= dc + j < M:
                        total += arr[dr+j][dc+j]
            total_list.append(total)

    print(f"#{tc} {total_list} {len(total_list)}")
    print(f"#{tc} {my_max(total_list)}")
