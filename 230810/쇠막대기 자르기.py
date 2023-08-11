import sys
sys.stdin = open("쇠막대기 자르기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = input()

    stack = []
    ans = 0
    idx = 0

    while idx < len(arr)-1:
        if arr[idx] == "(":
            if arr[idx+1] == "(":
                stack.append(arr[idx])
                ans += 1
                idx += 1
            else:
                ans += len(stack)
                idx += 2
        else:
            stack.pop()
            idx += 1

    print(f"#{tc} {ans}")