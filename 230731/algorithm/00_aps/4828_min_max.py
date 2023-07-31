import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for mx in arr:
        if max_v < mx:
            max_v = mx
    for mn in arr:
        if min_v > mn:
            min_v = mn
    ans = max_v - min_v

    print(f"#{tc} {ans}")
