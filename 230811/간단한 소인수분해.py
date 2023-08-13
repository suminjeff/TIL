import sys

sys.stdin = open("간단한 소인수분해.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    elements = [2, 3, 5, 7, 11]
    counts = []
    for e in elements:
        cnt = 0
        while N % e == 0:
            N = N // e
            cnt += 1
        counts.append(cnt)

    print(f"#{tc}", *counts)