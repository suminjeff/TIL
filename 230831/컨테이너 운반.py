import sys

sys.stdin = open("컨테이너 운반.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    delivered = [0] * N
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    weights.sort(reverse=True); trucks.sort(reverse=True)
    ans = 0
    while trucks:
        truck = trucks.pop(0)
        for i in range(N):
            if truck >= weights[i] and delivered[i] == 0:
                ans += weights[i]
                delivered[i] = 1
                break

    print(f"#{tc} {ans}")