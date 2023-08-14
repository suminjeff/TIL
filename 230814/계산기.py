import sys

sys.stdin = open("계산기1.txt", "r")


def to_postfix(expression):
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
    return res


def postfix(expression):
    stack = []
    a1 = 0
    a2 = 0
    for i in range(len(expression)):
        if expression[i].isnumeric():
            stack.append(int(expression[i]))
        elif expression[i] == "+":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 + a2)
        elif expression[i] == "-":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 - a2)
        elif expression[i] == "*":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 * a2)
        elif expression[i] == "/":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 / a2)
    return stack

T = 10

for tc in range(1, T + 1):
    length = int(input())
    phrase = list(input())
    expression = to_postfix(phrase)
    ans = postfix(expression)
    print(f"#{tc}", *ans)
