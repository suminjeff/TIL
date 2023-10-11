import sys

sys.stdin = open('숨바꼭질.txt', 'r')
input = sys.stdin.readline
from collections import deque

MAX = 10 ** 5

adj_l = {}

visited = [False] * (MAX + 1)
for i in range(MAX + 1):
    if i not in adj_l:
        adj_l.setdefault(i, set())
    if 0 <= i - 1 <= MAX:
        adj_l[i].add(i - 1)
    if 0 <= i + 1 <= MAX:
        adj_l[i].add(i + 1)
    if 0 <= 2 * i <= MAX:
        adj_l[i].add(2 * i)

N, K = map(int, input().split())
visited[N] = True
que = deque([[N, 0]])
while que:
    v, t = que.popleft()
    if v == K:
        print(t)
        break
    for w in adj_l[v]:
        if not visited[w]:
            visited[w] = True
            que.append([w, t + 1])
