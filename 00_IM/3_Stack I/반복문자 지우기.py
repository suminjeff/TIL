import sys

sys.stdin = open("반복문자 지우기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    top = -1
    for i in string:
        if stack:
            if i == stack[top]:
                stack.pop()
                top -= 1
            else:
                stack.append(i)
                top += 1
        else:
            stack.append(i)
            top += 1
    ans = len(stack)

    print(f"#{tc} {ans}")