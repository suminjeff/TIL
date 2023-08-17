import sys

sys.stdin = open("계산기2.txt", "r")


def push(item):
    global top
    top += 1
    stack[top] = item


def pop():
    global top
    tmp = stack[top]
    top -= 1
    return tmp


def isEmpty():
    return top == -1


def to_postfix(infix):
    numbers = '0123456789'
    icp = {"+": 1, "*": 2}
    isp = {"+": 1, "*": 2}

    postfix = ""

    for token in infix:
        if token in numbers:
            postfix += token
        else:
            while not isEmpty() and icp[token] <= isp[stack[top]]:
                


T = 10
for tc in range(1, T+1):
    size = int(input())
    infix = input()
    stack = [0] * size
    top = -1
    print(f"#{tc} {arr}")