import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    canvas = [[0 for row in range(10)] for col in range(10)]
    purple = 0
    for n in range(N):
        for row in range(10):
            for col in range(10):
                if arr[n][4] == 1:
                    if arr[n][0] <= row <= arr[n][2] and arr[n][1] <= col <= arr[n][3]:
                        if canvas[row][col] == 'blue':
                            canvas[row][col] = 'purple'
                            purple += 1
                        elif canvas[row][col] == 'purple':
                            canvas[row][col] = 'purple'
                        else:
                            canvas[row][col] = 'red'
                if arr[n][4] == 2:
                    if arr[n][0] <= row <= arr[n][2] and arr[n][1] <= col <= arr[n][3]:
                        if canvas[row][col] == 'red':
                            canvas[row][col] = 'purple'
                            purple += 1
                        elif canvas[row][col] == 'purple':
                            canvas[row][col] = 'purple'
                        else:
                            canvas[row][col] = 'blue'

    print(f"#{tc} {purple}")