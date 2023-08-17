import sys

sys.stdin = open("특별한 정렬.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    rra = list(reversed(arr))
    ans = []
    for i in range(5):
        ans.append(arr.pop())
        ans.append(rra.pop())

    print(f"#{tc}", *ans)