import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt', 'r')
input = sys.stdin.readline


def dfs(v, string, depth):
    if depth == 7:
        string_set.add(string)
        return
    r, c = v
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            dfs([nr, nc], string+arr[nr][nc], depth+1)


N = 4
T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(N)]
    string_set = set()
    for i in range(N):
        for j in range(N):
            dfs([i, j], arr[i][j], 1)
    print(f"#{tc} {len(string_set)}")