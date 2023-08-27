import sys

sys.stdin = open("자기 방으로 돌아가기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    corridor = [0]*200
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        if a % 2 == 0:
            a = a//2-1
        else:
            a = a//2
        if b % 2 == 0:
            b = b//2-1
        else:
            b = b//2
        start, end = min(a, b), max(a, b)
        for i in range(start, end+1):
            corridor[i] += 1
    ans = max(corridor)
    print(f"#{tc} {ans}")