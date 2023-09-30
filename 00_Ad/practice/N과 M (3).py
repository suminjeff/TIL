import sys
sys.stdin = open("N과 M (3).txt", "r")
input = sys.stdin.readline


def prod(cnt):
    if cnt == M:
        print(*arr)
        return
    for n in nums:
        arr[cnt] = n
        prod(cnt+1)


N, M = map(int, input().split())
arr = [0] * M
nums = [i for i in range(1, N+1)]
prod(0)