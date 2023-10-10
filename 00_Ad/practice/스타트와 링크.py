import sys
sys.stdin = open('스타트와 링크.txt', 'r')
input = sys.stdin.readline


def calc(vstd):
    v1 = v2 = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                if visited[i] and visited[j]:
                    v1 += arr[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    v2 += arr[i][j]
    return abs(v1-v2)


def dfs(depth, idx):
    global min_d
    if depth == N//2:
        min_d = min(min_d, calc(visited))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_d = float('inf')
dfs(0, 0)
print(min_d)