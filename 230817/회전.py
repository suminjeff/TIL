import sys

sys.stdin = open("회전.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    que = [0] + list(map(int, input().split()))
    front = 0
    rear = N

    for _ in range(M):
        front = (front+1) % (N+1)
        rear = (rear+1) % (N+1)
        que[rear] = que[front]
    ans = que[(front+1) % (N+1)]
    print(f"#{tc} {ans}")