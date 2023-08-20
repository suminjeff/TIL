import sys

sys.stdin = open("부분집합의 합.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [n for n in range(1, 13)]
    cnt = 0
    for i in range(1 << len(arr)):
        subset = []
        for j in range(i):
            if i & (1 << j):
                subset.append(arr[j])
        if len(subset) == N and sum(subset) == K:
            cnt += 1
    print(f"#{tc} {cnt}")