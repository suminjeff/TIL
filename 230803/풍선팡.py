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
    temp_list = []
    for row in range(N):
        for col in range(M):
            temp = arr[row][col]
            for delta in range(4):
                for flower in range(1, arr[row][col]+1):
                    dr = [0, flower, 0, -1 * flower]
                    dc = [flower, 0, -1 * flower, 0]
                    if 0 <= row + dr[delta] < N and 0 <= col + dc[delta] < M:
                        temp += arr[row + dr[delta]][col + dc[delta]]
            temp_list.append(temp)
    print(f"#{tc} {my_max(temp_list)}")
