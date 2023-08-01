import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # K = 1회 충전시 최대 이동 거리
    # N = 종점
    # M = 충전기 개수
    K, N, M = map(int, input().split())

    # charger = 시작점 + 충전기 위치 + 종점
    charger = [0] + list(map(int, input().split())) + [N]

    count = 0
    start = 0    # 충전을 하고 출발 하는 위치

    for i in range(1, M+2):
        if charger[i] - charger[i-1] > K:
            count = 0
            break
        if charger[i] - start > K:
            start = charger[i-1]
            count += 1

    print(f"#{tc} {count}")