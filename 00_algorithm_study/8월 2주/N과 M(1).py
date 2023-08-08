import sys

sys.stdin = open("N과 M(1).txt", "r")

N, M = map(int, input().split())
arr = [n + 1 for n in range(N)]

ans = []
for i in arr:
    temp = [i]
    for j in arr:
        temp.append(j)
    ans.append(temp)

for i in range(len(ans)):
    print(*ans[i])
