import sys

sys.stdin = open("피자 굽기.txt", "r")


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


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cQsize = N+1
    cQ = [0] * cQsize
    front = 0
    rear = 0
    undone = M
    done = []
    i = 0

    while len(done) < M:
        if isFull():
            melt = deQ()
            melt[1] //= 2
            enQ(melt)
            if cQ[rear][1] == 0:
                done.append(cQ[rear][0])
                rear = (rear - 1) % cQsize
        elif undone > 0:
            enQ([i, arr[i]])
            undone -= 1
            i += 1
        else:
            melt = deQ()
            melt[1] //= 2
            enQ(melt)
            if cQ[rear][1] == 0:
                done.append(cQ[rear][0])
                rear = (rear - 1) % cQsize
    print(f"#{tc} {done[-1] + 1}")

