def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')    # 디버깅 목적
    else:
        stack[top] = item


def pop():
    global top
    top -= 1
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]

    

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
push(20, size)
print(stack)
print(pop())
if top > -1:
    top -= 1
    print(stack[top+1])