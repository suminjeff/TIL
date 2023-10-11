import sys
sys.stdin = open('연결 요소.txt', 'r')
input = sys.stdin.readline


def find(x):
    if x != p[x]:
        return find(p[x])
    return p[x]


def union(x, y):
    x, y = find(x), find(y)
    p[max(x, y)] = min(x, y)


N, M = map(int, input().split())
p = [i for i in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    union(s, e)

cnt = 0
for i in range(1, N+1):
    if i == p[i]:
        cnt += 1
print(cnt)