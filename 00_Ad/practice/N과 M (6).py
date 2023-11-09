import sys

sys.stdin = open('N과 M (6).txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * N
ans = set()
for i in range(1, 1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(arr[j])
    if len(subset) == M:
        ans.add(tuple(subset))
ans = list(ans)
ans.sort()
for res in ans:
    print(*res)
