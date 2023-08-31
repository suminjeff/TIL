import sys

sys.stdin = open("화물 도크.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    input_arr.sort(key=lambda x: x[1])

    stack = []
    top = -1
    for i in range(N):
        s, e = input_arr[i]
        if stack:
            a, b = stack[top]
            if b <= s:
                stack.append([s, e])
                top += 1
        else:
            stack.append([s, e])
            top += 1
    print(f"#{tc} {top+1}")