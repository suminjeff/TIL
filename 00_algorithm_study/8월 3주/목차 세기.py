import sys

sys.stdin = open("목차 세기.txt", "r")


def push(item):
    global top
    global N

    top += 1
    if top == N:
        print('overflow')
    else:
        stack[top] = item


def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]


N = int(input())
arr = [int(input()) for _ in range(N)]

stack = [0] * N
top = -1

# for i in arr:
#     if not stack:
#         stack.append(i)
#     else:
#         if i == 1:
#             stack.pop()
#     elif
push(arr[0])

print(stack)