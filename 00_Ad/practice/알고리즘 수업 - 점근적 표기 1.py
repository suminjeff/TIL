import sys
sys.stdin = open("알고리즘 수업 - 점근적 표기 1.txt", "r")


def f(n):
    global a1
    global a0
    return a1*n + a0


def O(n):
    if n == 100:q
        return True
    else:
        if f(n) <= c * n:
            return O(n+1)
        else:
            return False

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
print(int(O(n0)))
