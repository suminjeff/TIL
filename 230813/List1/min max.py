import sys

sys.stdin = open("min max.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    max_v = 0
    min_v = 1000000
    for i in list(map(int, input().split())):
        if max_v < i:
            max_v = i
        if min_v > i:
            min_v = i
    ans = max_v - min_v

    print(f"#{tc} {ans}")