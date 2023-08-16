import sys
sys.stdin = open("삼성시의 버스 노선.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [0] * 5001
    ans = []
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            arr[i] += 1
    P = int(input())
    for _ in range(P):
        C = int(input())
        ans.append(arr[C])

    print(f"#{tc}", *ans)