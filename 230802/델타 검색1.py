import sys
sys.stdin = open("input.txt", "r")


def my_abs(value):
    if value > 0:
        return value
    else:
        return -1 * value


def delta_sum(num_list):
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(N):              # 행 탐색
        for j in range(N):          # 열 탐색
            for k in range(4):      # 방향(델타) 탐색
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    total += my_abs(arr[i][j] - arr[ni][nj])

    print(f"#{tc} {total}")
