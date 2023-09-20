import sys
from collections import deque
sys.stdin = open("연산.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    visited[N] = 1
    que = deque()
    que.append(N)
    while que:
        n = que.popleft()
        if n == M:
            break
        for i in [n + 1, n - 1, n * 2, n - 10]:
            if 0 <= i <= 1000000 and not visited[i]:
                visited[i] = visited[n] + 1
                que.append(i)
    ans = visited[M]
    print(f"#{tc} {ans}")