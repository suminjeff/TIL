import sys

sys.stdin = open("GNS.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    tc, N = input().split()
    arr = list(input().split())
    GNS = {"ZRO": 0,
           "ONE": 1,
           "TWO": 2,
           "THR": 3,
           "FOR": 4,
           "FIV": 5,
           "SIX": 6,
           "SVN": 7,
           "EGT": 8,
           "NIN": 9}
    print(tc)
    for i in range(10):
        for j in arr:
            if GNS[j] == i:
                print(j, end=" ")
    print()
