import sys
sys.stdin = open("LCS 2.txt", "r")
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

N, M = len(str1), len(str2)

dp = [0]*M
strCommon = []

for i in range(N):
    cnt = 0
    for j in range(M):
        if cnt < dp[j]:
            cnt = dp[j]
        elif str1[i] == str2[j]:
            dp[j] = cnt + 1
print(dp)
print(max(dp))