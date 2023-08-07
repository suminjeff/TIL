import sys
sys.stdin = open("GNS.txt", "r")

T = int(input())
alien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(1, T+1):
    tc, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))
    ans = []
    for i in alien:
        for j in arr:
            if j == i:
                ans.append(j)

    print(tc)
    print(*ans)