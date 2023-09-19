import sys
sys.stdin = open("격자판의 숫자 이어 붙이기.txt", "r")


def dfs(r, c, t, number):
    if t == 7:
        n_set.add(number)
        return
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, t+1, number+board[nr][nc])


T = int(input())
for tc in range(1, T+1):
    board = [input().split() for _ in range(4)]
    visited = [[0]*4 for _ in range(4)]
    n_set = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, board[i][j])

    ans = len(n_set)
    print(f"#{tc} {ans}")