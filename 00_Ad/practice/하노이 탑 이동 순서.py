import sys
sys.stdin = open("하노이 탑 이동 순서.txt", "r")
input = sys.stdin.readline

def hanoi(n, start, end, other):
    global cnt
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, other, end)
    print(start, end)
    hanoi(n-1, other, end, start)


N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)