import sys

sys.stdin = open("쇠막대기 자르기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = input()
    N = len(arr)

    stack = []
    ans = 0
    i = 0

    while i < N-1:
        if arr[i] == "(":
            if arr[i+1] == "(":
                stack.append(arr[i])
                ans += 1
                i += 1
            else:
                ans += len(stack)
                i += 2
        else:
            stack.pop()
            i += 1

    print(f"#{tc} {ans}")