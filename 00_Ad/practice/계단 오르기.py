import sys
sys.stdin = open('계단 오르기.txt', 'r')
input = sys.stdin.readline


# N = int(input())
# points = [0] + [int(input()) for _ in range(N)]
# idx = -1
# cnt = 0
# dp = [0] + [0]*N
# dp[1] = points[1]
# if N > 1:
#     dp[2] = points[1]+points[2]
#     if N >= 3:
#         for i in range(3, N+1):
#             dp[i] = max(dp[i-3]+points[i-1]+points[i], dp[i-2]+points[i])
# print(dp[-1])
# print(dp)

    # N = int(input())
    # stairs = [0] + [int(input()) for _ in range(N)]
    #
    # dp = [[0, 0] for _ in range(N+1)]
    # dp[N][1] = stairs[N]
    #
    # if len(stairs) == 2:
    #     print(stairs[N])
    # elif len(stairs) == 3:
    #     print(stairs[1]+stairs[2])
    # elif len(stairs) == 4:
    #     print(max(stairs[2]+stairs[3], stairs[1]+stairs[3]))
    # else:
    #     dp[N-1][0] = stairs[N-1] + stairs[N]
    #     dp[N-1][1] = stairs[N]
    #
    #     dp[N-2][0] = stairs[N-2] + stairs[N]
    #     dp[N-2][1] = stairs[N-2] + stairs[N]
    #
    #     for i in range(N-3, -1, -1):
    #         dp[i][0] = max(dp[i+2][0], dp[i+2][1]) + stairs[i]
    #         dp[i][1] = dp[i+1][0] + stairs[i]
    #
    #     case = [dp[0][0], dp[0][1], dp[1][0], dp[1][1]]
    #     print(max(case))
    # print(dp)

def climb(before, now, cnt, path):
    if now > N:
        return
    dp[now] = max(dp[now], path[before]+points[now])
    path[now] = path[before]+points[now]
    if cnt == 2:
        if now+2 <= N:
            climb(now, now+2, 1, path)
    else:
        if now+1 <= N:
            climb(now, now+1, cnt+1, path)
        if now+2 <= N:
            climb(now, now+2, 1, path)


N = int(input())
points = [0] + [int(input()) for _ in range(N)]
dp = [0] + [0]*N
climb(0, 0, 0, dp[:])
print(dp[-1])
print(dp)