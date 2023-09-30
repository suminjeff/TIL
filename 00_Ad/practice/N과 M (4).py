import sys
sys.stdin = open("N과 M (4).txt", "r")
input = sys.stdin.readline


def cwr(n, bucket, k):
    if k == 0:
        print(*bucket)
        return

    lastIndex = len(bucket) - k - 1

    if len(bucket) == k:
        smallest = 0
    else:
        smallest = bucket[lastIndex]

    for i in range(smallest, n):
        bucket[lastIndex+1] = nums[i]
        cwr(n, bucket, k-1)


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
cwr(N, [0]*M, M)