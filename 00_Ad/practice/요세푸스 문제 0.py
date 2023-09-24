import sys
sys.stdin = open("요세푸스 문제 0.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [n for n in range(1, N+1)]
visited = [0] * (N+1)
i = K-1
remaining = N
ans = []
while arr:
    ans.append(arr[i])
    visited[arr[i]] = 1
    remaining -= 1
    if remaining == 0:
        break
    for _ in range(K):
        i = (i + 1) % N
        if visited[arr[i]]:
            while visited[arr[i]]:
                i = (i + 1) % N
print("<", end="")
print(*ans, sep=", ", end="")
print(">")