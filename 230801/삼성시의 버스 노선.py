import sys

sys.stdin = open("삼성시의 버스 노선.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0 for _ in range(5001)]
    for i in range(N):
        A, B = map(int, input().split())
        for k in range(A, B+1):
            arr[k] += 1
    P = int(input())
    result = []
    for j in range(P):
        C = int(input())
        result.append(arr[C])
    print(f"#{tc}", *result)