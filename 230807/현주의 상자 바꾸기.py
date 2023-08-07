import sys
sys.stdin = open("현주의 상자 바꾸기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            arr[i] = q

    print(f"#{tc}", end=" ")
    print(*arr)
