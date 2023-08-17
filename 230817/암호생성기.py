import sys

sys.stdin = open("암호생성기.txt", "r")


def enQ(item):
    global rear
    global cQsize
    if isFull():
        print("Q_Full")
    else:
        rear = (rear + 1) % cQsize
        cQ[rear] = item


def deQ():
    global front
    if isEmpty():
        print("Q_Empty")
    else:
        front = (front + 1) % cQsize
        return cQ[front]


def isEmpty():
    global front
    global rear

    return front == rear


def isFull():
    global front
    global rear
    return (rear + 1) % cQsize == front


def Qpeek():
    global front
    if isEmpty():
        print("Q_Empty")
    else:
        return cQ[front + 1]


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    arr = list(map(int, input().split()))
    N = 8
    cQsize = N+1
    cQ = [0] * cQsize
    front = 0
    rear = 0
    for i in arr:
        enQ(i)
    subtract = [n for n in range(1, 6)]
    ans = []
    i = 0
    while cQ[rear] > 0:
        enQ(deQ()-subtract[i])
        i = (i+1) % 5
        if cQ[rear] <= 0:
            cQ[rear] = 0
            while not isEmpty():
                ans.append(deQ())
            break

    print(f"#{tc}", *ans)
