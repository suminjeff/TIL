import sys

sys.stdin = open("직사각형.txt", "r")

T = 4
for tc in range(1, T+1):
    x_max = y_max = 0
    Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2 = map(int, input().split())
    if x_max < Ax2:
        x_max = Ax2
    if x_max < Bx2:
        x_max = Bx2
    if y_max < Ay2:
        y_max = Ay2
    if y_max < By2:
        y_max = By2

    grid = [[0]*(x_max + 1) for _ in range(y_max + 1)]
    for row in range(Ay1, Ay2+1):
        for col in range(Ax1, Ax2+1):
            grid[row][col] = 1

    for row in range(By1, By2+1):
        for col in range(Bx1, Bx2+1):
            if grid[row][col] == 1:
                grid[row][col] = 2

    tmp = []
    for row in range(y_max+1):
        if grid[row].count(2) > 0:
            tmp.append(grid[row].count(2))

    ans = ''
    if len(tmp) == 0:
        ans = 'd'
    elif len(tmp) == 1:
        if tmp[0] == 1:
            ans = 'c'
        else:
            ans = 'b'
    else:
        if len(tmp) == sum(tmp):
            ans = 'b'
        else:
            ans = 'a'
    print(ans)