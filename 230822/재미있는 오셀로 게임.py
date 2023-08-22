import sys

sys.stdin = open("재미있는 오셀로 게임.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2 - 1] = 1
    dr = [0, 1, 0, -1, 1, -1, -1, 1]
    dc = [1, 0, -1, 0, -1, -1, 1, 1]

    opponent = {1: 2, 2: 1}

    for _ in range(M):
        x, y, color = map(int, input().split())
        row = y-1
        col = x-1
        arr[row][col] = color
        for k in range(8):
            nr = row + dr[k]
            nc = col + dc[k]
            stack = []
            while True:
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == opponent[color]:
                        stack.append([nr, nc])
                        nr += dr[k]
                        nc += dc[k]
                    elif arr[nr][nc] == color:
                        if stack:
                            r, c = stack.pop()
                            arr[r][c] = color
                        else:
                            break
                    else:
                        break
                else:
                    break
    black = 0
    white = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 1:
                black += 1
            elif arr[row][col] == 2:
                white += 1
    print(f"#{tc} {black} {white}")