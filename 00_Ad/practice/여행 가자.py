import sys

sys.stdin = open('여행 가자.txt', 'r')
input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return find(parents[x])


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N = int(input())
M = int(input())
adj_l = [[] for _ in range(N + 1)]
parents = [i for i in range(N + 1)]

for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j in range(N):
        if info[j] == 1:
            adj_l[i].append(j + 1)
            union(i, j + 1)
plan = list(map(int, input().split()))

root = -1
ans = 'YES'
for i in range(len(plan)):
    if i == 0:
        root = parents[plan[i]]
    else:
        if parents[plan[i]] != root:
            ans = 'NO'
            break

# print(parents)
# print(adj_l)
# print(plan)
print(ans)