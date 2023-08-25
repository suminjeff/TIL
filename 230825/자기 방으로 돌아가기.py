import sys

sys.stdin = open('자기 방으로 돌아가기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [0]*201
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = (a+a%2)//2, (b+b%2)//2
        s, e = min(a, b), max(a, b)
        for i in range(s, e+1):
            arr[i] += 1

    print(f"#{tc} {max(arr)}")