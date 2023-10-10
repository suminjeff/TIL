import sys
sys.stdin = open('바이러스.txt', 'r')
input = sys.stdin.readline


def dfs(v):
    for w in adj_l[v]:
        if w and not visited[w]:
            visited[w] = 1
            dfs(w)


N = int(input())
M = int(input())
adj_l = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    s, e = map(int, input().split())
    adj_l[s].append(e)
    adj_l[e].append(s)
s = 1
visited[s] = 1
dfs(s)
print(sum(visited)-1)