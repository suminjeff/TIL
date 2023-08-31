import sys

sys.stdin = open("부분 수열의 합.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(arr[j])
        if sum(subset) == K:
            cnt += 1
    print(f"#{tc} {cnt}")