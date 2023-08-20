import sys

sys.stdin = open("후위 유사 표기법.txt", "r")

op = {"+": 1, "-": 1, "*": 2, "/": 2}

T = int(input())
for tc in range(1, T+1):
    infix = input()
    postfix = ""
    stack = []
    for tkn in infix:
        if tkn in "0123456789":
            postfix += tkn
        else:
            stack.append(tkn)
    while stack:
        postfix += stack.pop()

    print(f"#{tc} {postfix}")