import sys

sys.stdin = open("후위 표기법.txt", "r")

T = int(input())
for tc in range(1, T+1):
    expression = list(input())
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    res = ""
    stack = []
    for i in expression:
        if i.isnumeric():
            res += i
        elif i in priority:
            if stack and (priority[i] <= priority[stack[-1]]):
                res += stack.pop()
            stack.append(i)
    while stack:
        res += stack.pop()

    print(f"#{tc} {res}")