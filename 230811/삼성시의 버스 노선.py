import sys

sys.stdin = open("삼성시의 버스 노선.txt", "r")

T = int(input())
for tc in range(1, T+1):
    bus_stop = [0] * 5001

    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_stop[i] += 1
    P = int(input())
    ans = []
    for _ in range(P):
        ans.append(bus_stop[int(input())])
    print(f"#{tc}", *ans)