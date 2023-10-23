import sys
sys.stdin = open('플로이드.txt', 'r')
input = sys.stdin.readline

inf = float("inf")


N = int(input())
M = int(input())
distance = [[inf]*N for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    distance[s-1][e-1] = min(distance[s-1][e-1], w)

for i in range(N):
    for j in range(N):
        if i == j:
            distance[i][j] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(N):
    for j in range(N):
        if distance[i][j] == inf:
            distance[i][j] = 0

visited = [0]*N
for i in range(N):
    print(*distance[i])