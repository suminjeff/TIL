import sys
sys.stdin = open("소인수분해.txt", "r")

N = int(input())
div = 2
while N != 1:
    if N % div == 0:
        print(div)
        N //= div
    else:
        div += 1