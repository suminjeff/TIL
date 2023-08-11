import sys

sys.stdin = open("스도쿠 검증.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 1

    for row in range(9):
        cnt = [0]*10
        for col in range(9):
            cnt[arr[row][col]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                ans = 0
                break

    for col in range(9):
        cnt = [0] * 10
        for row in range(9):
            cnt[arr[row][col]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                ans = 0
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * 10
            for row in range(i, i+3):
                for col in range(j, j+3):
                    cnt[arr[row][col]] += 1
            for k in range(1, 10):
                if cnt[k] == 0:
                    ans = 0
                    break

    print(f"#{tc} {ans}")


#1 1
#2 0
#3 1
#4 0
#5 0
#6 1
#7 0
#8 1
#9 1
#10 0
