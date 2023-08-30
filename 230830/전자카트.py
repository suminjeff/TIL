import sys

sys.stdin = open("전자카트.txt", "r")

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = [n for n in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    possible_routes = []
    for perm in permutations(N_list, N):
        if perm[0] == 0:
            possible_routes.append(list(perm))
    ans = float("inf")
    for route in possible_routes:
        usage = 0
        for i in range(N):
            usage += arr[route[i]][route[(i+1) % N]]
        ans = min(ans, usage)
    print(f"#{tc} {ans}")