import sys
sys.stdin = open("장훈이의 높은 선반.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    min_diff = float('inf')
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(S[j])
        if sum(subset) >= B:
            diff = abs(sum(subset) - B)
            if min_diff > diff:
                min_diff = diff

    print(f"#{tc} {min_diff}")