import sys

sys.stdin = open('알파벳.txt', 'r')
input = sys.stdin.readline

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dfs(r, c, depth, visited):
    global max_depth
    max_depth = max(max_depth, depth)
    v = arr[r][c]
    visited[v] = 1
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            nv = arr[nr][nc]
            if alphabet[arr[nr][nc]] == 0:
                dfs(nr, nc, depth + 1, visited)
                visited[nv] = 0


alphabet = {chr(x): 0 for x in range(65, 91)}
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
max_depth = 0
r = c = 0
alphabet[arr[r][c]] = 1
dfs(r, c, 1, alphabet)
print(max_depth)
