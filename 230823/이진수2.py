import sys

sys.stdin = open('이진수2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    dec = float(input())
    stack = []
    i = -1
    while dec:
        stack.append(int(dec//2**i))
        dec %= 2**i
        i -= 1
    if len(stack) > 12:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc}", end=" ")
        print(*stack, sep="")