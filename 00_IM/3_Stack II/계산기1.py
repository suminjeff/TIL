import sys

sys.stdin = open("계산기1.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    stack = []
    postfix = ""
    for token in arr:
        if token in "0123456789":
            postfix += token
        else:
            if stack:
                postfix += stack.pop()
            stack.append(token)
    while stack:
        postfix += stack.pop()

    stack = []
    for token in postfix:
        if token in "0123456789":
            stack.append(token)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a+b)
    ans = stack[0]
    print(f"#{tc} {ans}")