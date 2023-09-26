import sys
sys.stdin = open("미생물 격리.txt", "r")
input = sys.stdin.readline
from collections import deque


direction = {
    1: [-1, 0, 2],
    2: [1, 0, 1],
    3: [0, -1, 4],
    4: [0, 1, 5]
}


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    que = deque()
    total = 0
    for _ in range(K):
        info = list(map(int, input().split()))
        que.append(info)
        r, c, n, d = info
        arr[r][c] += n
        total += n

    # while que:
    #     if M == 0:
    #         break
    #     cluster = {}
    #     for _ in range(len(que)):
    #         r, c, n, d = que.popleft()
    #         r += direction[d][0]
    #         c += direction[d][1]
    #         if r == 0 or r == N-1 or c == 0 or c == N-1:
    #             d = direction[d][2]
    #             n //= 2
    #             total -= n - n//2
    #         if n == 0:
    #             continue
    #
    #         if (r, c) in cluster.keys():
    #             cluster[(r, c)].append([n, d])
    #         else:
    #             cluster.setdefault((r, c), [[n, d]])
    #     for k, v in cluster.items():
    #         r, c = k
    #         if len(v) == 1:
    #             n, d = v[0][0], v[0][1]
    #             que.append([r, c, n, d])
    #         else:
    #             n = 0
    #             max_n = 0
    #             d = 0
    #             for i in range(len(v)):
    #                 n += v[i][0]
    #                 if max_n < v[i][0]:
    #                     max_n = v[i][0]
    #                     d = v[i][1]
    #             que.append([r, c, n, d])
    #     M -= 1


    # print(f"#{tc} {total}")