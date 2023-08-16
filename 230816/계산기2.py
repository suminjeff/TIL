import sys

sys.stdin = open("계산기2.txt", "r")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    op = {"+": 1, "*": 2}
    stack = []
    res = []
    for i in arr:
        if i.isnumeric():
            res.append(int(i))
        elif i in op:
            if stack and op[i] <= op[stack[-1]]:
                res.append(stack.pop())
            stack.append(i)
    while stack:
        res.append(stack.pop())

    for i in res:
        if i in op:
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    calc = a + b
                else:
                    calc = a * b
                stack.append(calc)
        else:
            stack.append(i)

    ans = stack[0]

    print(f"#{tc} {ans}")