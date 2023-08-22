import sys

sys.stdin = open("재미있는 오셀로 게임.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    dr = [0, 1, 0, -1, 1, -1, -1, 1]
    dc = [1, 0, -1, 0, -1, -1, 1, 1]

    opponent = {1: 2, 2: 1}

    for _ in range(M):
        zero_cnt = N*N - 4
        if zero_cnt == 0:
            break
        x, y, color = map(int, input().split())
        row = y-1
        col = x-1
        if board[row][col] == 0:
            board[row][col] = color
            for k in range(8):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    while board[nr][nc] != color:
                        nr += dr[k]
                        nc += dc[k]
                        if board[nr][nc] == color:
                            while 


    black = 0
    white = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                black += 1
            elif board[row][col] == 2:
                white += 1
    print(board)
    print(f"#{tc} {black} {white}")