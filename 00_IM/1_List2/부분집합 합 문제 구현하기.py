import sys

sys.stdin = open("부분집합 합 문제 구현하기.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    ans = False
    subset = []
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])
        subset.append(temp)

    for i in subset:
        if len(i) > 0 and sum(i) == 0:
            ans = True
            break

    print(f"#{tc} {int(ans)}")