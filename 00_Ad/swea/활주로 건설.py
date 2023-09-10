import sys

sys.stdin = open("활주로 건설.txt", "r")


def check(r, N):
    stack = []
    top = -1
    max_v = max(arr[r])
    for c in range(N):
        if arr[r][c] != max_v:
            if stack:
                if stack[top] ==
            else:
                stack.append(arr[r][c])
        else:
            stack.clear()
            top = -1





T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 행 방향



    # 열방향


    print(f"#{tc} {ans}")