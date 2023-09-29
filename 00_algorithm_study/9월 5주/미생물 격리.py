import sys
sys.stdin = open("미생물 격리.txt", "r")
input = sys.stdin.readline
from collections import deque


# 1 = 상, 2 = 하, 3 = 좌, 4 = 우
direction = {
    1: [-1, 0, 2],
    2: [1, 0, 1],
    3: [0, -1, 4],
    4: [0, 1, 3]
}


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    # 데크에 군집들 정보 담기
    que = deque()
    total = 0
    for _ in range(K):
        info = list(map(int, input().split()))
        total += info[2]
        que.append(info)

    # M 시간 동안 미생물 활동
    while que:
        if M == 0:
            break
        coordinates = {}
        for _ in range(len(que)):
            r, c, n, d = que.popleft()
            r, c = r + direction[d][0], c + direction[d][1]
            if r == 0 or c == 0 or r == N-1 or c == N-1:
                total -= n - n//2
                n //= 2
                d = direction[d][2]
                if n == 0:
                    continue
            if (r, c) in coordinates:
                coordinates[(r, c)][d] = n
            else:
                coordinates.setdefault((r, c), [0]*5)
                coordinates[(r, c)][d] = n
        for k, v in coordinates.items():
            r, c = k
            n, d = sum(v), v.index(max(v))
            que.append([r, c, n, d])
        M -= 1

    print(f"#{tc} {total}")