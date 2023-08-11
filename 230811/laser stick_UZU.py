import sys
sys.stdin = open("laser stick_UZU.txt", "r")

T = int(input())
for tc in range(1, T+1):
    laser = list(input())
    stack = []
    stick = 0
    laser_position = []

    for j in range(len(laser)):

        if j+1 < len(laser):
            if laser[j-1] == '(' and laser[j] == ')':
                laser_position.append(j)

    for i in range(len(laser)):
        if laser[i] == '(':
            stack.append(laser[i])
            stick += 1

        elif laser[i] == ')':
            stack.pop()

            if i in laser_position:
                stick += len(stack)
                stick -= 1

    print(f'#{tc} {stick}')