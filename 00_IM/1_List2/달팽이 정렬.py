import sys

sys.stdin = open("달팽이 정렬.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        arr.extend(list(map(int, input().split())))

    for i in range(N*N):
        for j in range(N*N-1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    snail = [[0]*N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    idx = 0

    row = 0
    col = 0
    for i in range(N*N):
        snail[row][col] = arr[i]
        row += dr[idx]
        col += dc[idx]
        if row < 0 or col < 0 or row >= N or col >= N or snail[row][col] != 0:
            row -= dr[idx]
            col -= dc[idx]
            idx = (idx + 1) % 4
            row += dr[idx]
            col += dc[idx]

    print(f"#{tc}")
    for i in range(N):
        print(*snail[i])