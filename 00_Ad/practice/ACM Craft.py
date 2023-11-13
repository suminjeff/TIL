import sys

sys.stdin = open('ACM Craft.txt', 'r')
input = sys.stdin.readline
import heapq
from collections import deque


# def ACM_craft(start):
#     que = deque()
#     que.append([time[start-1], start])
#     min_time[start] = time[start-1]
#     while que:
#         t, x = que.popleft()
#         for nt, nx in adj_l[x]:
#             if t+nt < min_time[nx]:
#                 continue
#             min_time[nx] = t+nt
#             que.append([t+nt, nx])

def ACM_craft(start):
    heap = []
    heapq.heappush(heap, [time[start - 1] * -1, start])
    while heap:
        t, x = heapq.heappop(heap)
        t *= -1
        for nt, nx in adj_l[x]:
            if t + nt < min_time[nx]:
                continue
            min_time[nx] = t + nt
            heapq.heappush(heap, [(t + nt) * (-1), nx])


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return find(parent[x])


def union(x, y):
    x, y = find(x), find(y)
    parent[y] = x


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    min_time = [0] * (N + 1)
    for i in range(1, N + 1):
        min_time[i] = time[i - 1]
    adj_l = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(K):
        s, e = map(int, input().split())
        adj_l[s].append([time[e - 1], e])
        union(s, e)
    W = int(input())
    S = -1
    for i in range(1, N + 1):
        if i == parent[i] and parent.count(i) > 1:
            S = i
    ACM_craft(S)
    # print(parent)
    # print(f"#{tc} {min_time}, {W}")
    # print(f"#{tc} {min_time[W]}")
    print(min_time[W])
