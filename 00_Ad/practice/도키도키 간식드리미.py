import sys
sys.stdin = open("도키도키 간식드리미.txt", "r")
input = sys.stdin.readline


def wait(que, N):
    turn = 1
    stack = []
    while que:
        if que[0] == turn:
            que.pop(0)
            turn += 1
        else:
            stack.append(que.pop(0))

        while stack:
            if stack[-1] == turn:
                stack.pop()
                turn += 1
            else:
                break
    if not stack:
        return "Nice"
    else:
        return "Sad"


N = int(input())
que = list(map(int, input().split()))
print(wait(que, N))