import sys

sys.stdin = open("전기버스.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = [0] * (N+1)
    for i in list(map(int, input().split())):
        arr[i] = 1
    start = 0
    stop = K
    cnt = 0
    while 0 <= stop < N:
        if arr[stop] == 1:
            start = stop
            stop += K
            cnt += 1
        else:
            stop -= 1
            if start == stop:
                cnt = 0
                break
    print(f"#{tc} {cnt}")
