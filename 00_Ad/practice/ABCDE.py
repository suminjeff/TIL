import sys
sys.stdin = open('ABCDE.txt', 'r')
input = sys.stdin.readline


def dfs(x, n):
    if n >= 5:
        return
    for nx in relation[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx, n+1)


N, M = map(int, input().split())
parents = [i for i in range(N)]
relation = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
for i in range(N):
    visited = [0]*N
    visited[i] = 1
    dfs(i, 1)
    print(visited)