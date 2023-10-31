import sys
sys.stdin = open("01타일.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [0]*1000001
dp[1] = 1
dp[2] = 2
for k in range(3, N+1):
    dp[k] = (dp[k-1]+dp[k-2])%15746
print(dp[N])