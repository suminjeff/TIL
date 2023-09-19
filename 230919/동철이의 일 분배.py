import sys
sys.stdin = open("동철이의 일 분배.txt", "r")


def backtrack(i, P):
    global N
    global max_P
    if P <= max_P:
        return
    elif i == N:
        max_P = max(max_P, P)
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            backtrack(i+1, P*arr[i][j]*0.01)
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_P = 0
    backtrack(0, 1)
    print(f"#{tc} {max_P * 100:.6f}")