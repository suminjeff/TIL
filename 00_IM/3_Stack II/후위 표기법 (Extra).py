import sys

sys.stdin = open("후위 표기법 (Extra).txt", "r")


op = {"+": 1, "-": 1, "*": 2, "/": 2}

T = int(input())
for tc in range(1, T+1):
    infix = input()
    stack = []
    ans = ""
    for token in infix:
        if token.isnumeric():
            ans += token
        else:
            if stack and op[token] <= op[stack[-1]]:
                ans += stack.pop()
            stack.append(token)
    while stack:
        ans += stack.pop()

    print(f"#{tc} {ans}")