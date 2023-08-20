import sys

sys.stdin = open("숫자 배열 회전.txt", "r")


def turn90(arr):
    global N
    result = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            result[row][col] = arr[N-col-1][row]
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = turn90(arr)
    b = turn90(a)
    c = turn90(b)
    print(f"#{tc}")
    for row in range(N):
        print(*a[row], sep="", end=" ")
        print(*b[row], sep="", end=" ")
        print(*c[row], sep="", end=" ")
        print()