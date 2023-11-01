import sys
sys.stdin = open('특정 거리의 도시 찾기.txt', 'r')
input = sys.stdin.readline

from collections import deque

inf = int(10e9)


def bfs(start):
    distance[start] = 0
    visited[start] = True
    que = deque([start])
    while que:
        v = que.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                distance[w] = distance[v] + 1
                que.append(w)
            elif visited[w] and distance[w] > distance[v]+1:
                distance[w] = distance[v] + 1

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
distance = [inf]*(N+1)
visited = [False]*(N+1)
bfs(X)
ans = []
for i in range(1, N+1):
    if distance[i] == K:
        ans.append(i)
if ans:
    print(*ans, sep='\n')
else:
    print(-1)
# print(distance)