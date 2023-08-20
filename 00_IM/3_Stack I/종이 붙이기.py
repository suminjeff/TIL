import sys

sys.stdin = open("종이 붙이기.txt", "r")


def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return dp(n-1) + dp(n-2)*2


T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    ans = dp(N)
    print(f"#{tc} {ans}")
