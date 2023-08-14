import sys

sys.stdin = open("Forth.txt", "r")

T = int(input())
for tc in range(1, T+1):
    expression = list(input().split())
    try:
        stack = []
        a1 = 0
        a2 = 0
        for i in range(len(expression)):
            if expression[i].isnumeric():
                stack.append(int(expression[i]))
            elif expression[i] == "+":
                if len(stack) > 1:
                    a1 = stack.pop()
                    a2 = stack.pop()
                    stack.append(a1 + a2)
            elif expression[i] == "-":
                if len(stack) > 1:
                    a1 = stack.pop()
                    a2 = stack.pop()
                    stack.append(a1 - a2)
            elif expression[i] == "*":
                if len(stack) > 1:
                    a1 = stack.pop()
                    a2 = stack.pop()
                    stack.append(a1 * a2)
            elif expression[i] == "/":
                if len(stack) > 1:
                    a1 = stack.pop()
                    a2 = stack.pop()
                    stack.append(int(a1 / a2))
            elif expression[i] == '.':
                if len(stack) == 1:
                    print(f"#{tc} {stack.pop()}")
                else:
                    print(f"#{tc} error")
    except:
        print(f"#{tc} error")
