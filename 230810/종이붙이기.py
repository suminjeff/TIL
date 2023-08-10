import sys

sys.stdin = open("종이붙이기.txt", "r")


def fibo(n):
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 3
    for i in range(3, n+1):
        global cnt
        cnt += 1
        f[i] = f[i-1] + f[i-2] * 2

    return f[n]


T = int(input())

for tc in range(1, T+1):
    n = int(input())//10
    cnt = 0
    ans = fibo(n)
    print(f"#{tc} {ans}")
