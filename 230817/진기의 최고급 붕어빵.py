import sys

sys.stdin = open("진기의 최고급 붕어빵.txt", "r")

T = int(input())

for tc in range(1, T+1): 
    # N = 인원수, M초에 K개 붕어빵을 만들 수 있음
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    arr = [0] * (max(time)+1)
    for t in time:
        arr[t] += 1
    que = []
    flag = "Possible"
    for sec in range(max(time)+1):
        # M초마다 K개 붕어빵을 que에 대기시키기
        if sec % M == 0 and sec > 0:
                for _ in range(K):
                    que.append(1)

        if arr[sec] > 0:
            if sec == 0:
                flag = "Impossible"
            if que:
                while arr[sec] != 0:
                    que.pop(0)
                    arr[sec] -= 1
            else:
                flag = "Impossible"
                break

    print(f"#{tc} {flag}")