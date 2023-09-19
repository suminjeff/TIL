import sys
sys.stdin = open("전기버스2.txt", "r")


def bus(station, cnt):
    global min_cnt
    global N

    if station >= N-1:
        cnt -= 1
        min_cnt = min(cnt, min_cnt)
        return
    elif cnt >= min_cnt:
        return
    fuel = input_arr[station]
    for i in range(1, fuel+1):
        bus(station+i, cnt+1)

T = int(input())
for tc in range(1, T+1):
    N, *input_arr = list(map(int, input().split()))
    min_cnt = float('inf')
    bus(0, 0)
    print(f"#{tc} {min_cnt}")