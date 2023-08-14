import sys

sys.stdin = open("후위 유사 표기법 연습.txt", "r")

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
            stack.append(i)
    while stack:
        res += stack.pop()

    print(f"#{tc} {res}")