import sys
sys.stdin = open('DFS와 BFS.txt', 'r')
input = sys.stdin.readline


def dfs(v):
    visited_dfs[v] = 1
    track_dfs.append(v)
    for w in adj_l[v]:
        if not visited_dfs[w]:
            dfs(w)


def bfs(s):
    que = [s]
    visited_bfs[s] = 1
    while que:
        v = que.pop(0)
        track_bfs.append(v)
        for w in adj_l[v]:
            if w and not visited_bfs[w]:
                visited_bfs[w] = 1
                que.append(w)


N, M, V = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)
track_dfs = []
track_bfs = []
for _ in range(M):
    s, e = map(int, input().split())
    adj_l[s].append(e)
    adj_l[s].sort()
    adj_l[e].append(s)
    adj_l[e].sort()
dfs(V)
print(*track_dfs)
bfs(V)
print(*track_bfs)