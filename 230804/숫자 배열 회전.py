import sys

sys.stdin = open("숫자 배열 회전.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    turn90 = [[0] * N for _ in range(N)]
    turn180 = [[0] * N for _ in range(N)]
    turn270 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            turn90[j][N-1 - i] = arr[i][j]
            turn180[N-1 - i][N-1 - j] = arr[i][j]
            turn270[N-1 - j][i] = arr[i][j]

    string_list = [[] for r in range(N)]
    for i in range(N):
        string90 = ""
        string180 = ""
        string270 = ""
        for j in range(N):
            string90 += str(turn90[i][j])
            string180 += str(turn180[i][j])
            string270 += str(turn270[i][j])
        string_list[i].append(string90)
        string_list[i].append(string180)
        string_list[i].append(string270)

    print(f"#{tc}")
    for i in range(N):
        print(string_list[i])
