import sys

sys.stdin = open("Forth.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    expression = list(input().split())
    i = 0
    stack = []
    while True:
        if expression[i] in "+-*/":
            if len(stack) > 1:
                if expression[i] == "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                    i += 1
                elif expression[i] == "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                    i += 1
                elif expression[i] == "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                    i += 1
                elif expression[i] == "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a // b)
                    i += 1
            else:
                print(f"#{tc} error")
                break
        elif expression[i] == ".":
            if len(stack) == 1:
                print(f"#{tc} {stack[0]}")
                break
            else:
                print(f"#{tc} error")
                break
        else:
            stack.append(int(expression[i]))
            i += 1
