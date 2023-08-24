import sys

sys.stdin = open('Magnetic.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for col in range(N):
        row = 0
        while row < 100:
            if arr[row][col] == 1:
                while arr[row][col] != 2:
                    row += 1
                    if row == 100:
                        break
                if row < 100:
                    if arr[row][col] == 2:
                        cnt += 1
                        row += 1
            else:
                while arr[row][col] != 1:
                    row += 1
                    if row == 100:
                        break
    print(f"#{tc} {cnt}")