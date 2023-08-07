import sys

sys.stdin = open("달팽이 정렬.txt", "r")


def selection_sort(arr, n):
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    my_arr = []
    for n in range(N):
        my_arr += list(map(int, input().split()))

    selection_sort(my_arr, N*N)

    # 델타 탐색 (우 하 좌 상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0

    delta = 0

    arr = [[0]*N for _ in range(N)]

    for n in range(N*N):
        arr[r][c] = my_arr[n]
        r += dr[delta]
        c += dc[delta]
        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != 0:
            r -= dr[delta]
            c -= dc[delta]

            delta = (delta + 1) % 4

            r += dr[delta]
            c += dc[delta]

    print(f"#{tc}")
    for i in range(N):
        print(*arr[i])