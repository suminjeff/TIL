import sys
sys.stdin = open("ACM 호텔.txt", "r")
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    cnt = 0
    for col in range(W):
        for row in range(H):
            cnt += 1
            if cnt == N:
                ans = str(row+1) + str(col+1).zfill(2)
                print(ans)
                break
