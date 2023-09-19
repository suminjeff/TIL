import sys
sys.stdin = open("최소 생산 비용.txt", "r")


def backtrack(product, cost):
    global min_cost
    global N

    if cost >= min_cost:
        return
    elif product == N:
        min_cost = min(min_cost, cost)
    for factory in range(N):
        if not visited[factory]:
            visited[factory] = 1
            backtrack(product+1, cost+arr[product][factory])
            visited[factory] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_cost = float('inf')
    backtrack(0, 0)
    print(f"#{tc} {min_cost}")