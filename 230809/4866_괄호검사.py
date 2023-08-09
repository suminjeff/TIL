import sys
sys.stdin = open("4866_괄호검사.txt", "r")


def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] == item


def pop():
    global top
    top -= 1
    if top == -1:
        print('underflow!')
    else:
        return stack[top+1]


T = int(input())
for tc in range(1, T+1):
    case = list(input())
    size = len(case)
    stack = []
    idx = 0
    while idx < size:
        if case[idx] == "(":
            stack.append(case[idx])
            idx += 1
        elif case[idx] == ")":
            stack.pop()
            idx += 1
        elif case[idx] == "'":
            while case[idx+1] != "'":
                idx += 1
            idx += 2
        else:
            idx += 1
    if not stack:
        ans = 1
    else:
        ans = 0
    print(f"#{tc} {ans}")