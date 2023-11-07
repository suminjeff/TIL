import sys
sys.stdin = open('마인크래프트.txt', 'r')
input = sys.stdin.readline


# 입력값
N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans_t = float('inf')
ans_level = 0
for level in range(257):
    add = 0
    take = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] > level:
                take += arr[r][c] - level
            else:
                add += level - arr[r][c]
    if add > take + B:
        continue
    count = take * 2 + add
    if count <= ans_t:
        ans_t = count
        ans_level = level