import sys

sys.stdin = open('오목 판정.txt', 'r')


def five(arr):
    global N
    colors = ['o']
    for color in colors:
        # 가로
        for r1 in range(N):
            cons_r = 0
            for c1 in range(N):
                if arr[r1][c1] == color:
                    cons_r += 1
                    if cons_r >= 5:
                        return "YES"
                else:
                    cons_r = 0
        # 세로
        for c2 in range(N):
            cons_c = 0
            for r2 in range(N):
                if arr[r2][c2] == color:
                    cons_c += 1
                    if cons_c >= 5:
                        return "YES"
                else:
                    cons_c = 0
        # 양 대각
        for r3 in range(N):
            for c3 in range(N):
                if arr[r3][c3] == color:
                    cnt_down = 0
                    for k in range(1, 5):
                        nr1 = r3 + k
                        nc1 = c3 + k
                        if 0 <= nr1 < N and 0 <= nc1 < N:
                            if arr[nr1][nc1] == color:
                                cnt_down += 1
                            else:
                                break
                        else:
                            break
                    if cnt_down == 4:
                        return "YES"

                    cnt_up = 0
                    for m in range(1, 5):
                        nr2 = r3 - m
                        nc2 = c3 + m
                        if 0 <= nr2 < N and 0 <= nc2 < N:
                            if arr[nr2][nc2] == color:
                                cnt_up += 1
                            else:
                                break
                        else:
                            break
                    if cnt_up == 4:
                        return "YES"
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = five(arr)
    print(f"#{tc} {ans}")