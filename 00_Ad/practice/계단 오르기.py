import sys
sys.stdin = open('계단 오르기.txt', 'r')
input = sys.stdin.readline


N = int(input())
points = [0] + [int(input()) for _ in range(N)]
idx = -1
cnt = 0
dp = [0] + [0]*N
dp[1] = points[1]
if N > 1:
    dp[2] = points[1]+points[2]
    if N >= 3:
        for i in range(3, N+1):
            dp[i] = max(dp[i-3]+points[i-1]+points[i], dp[i-2]+points[i])
print(dp[-1])