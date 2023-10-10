import sys
sys.stdin = open("신나는 함수 실행.txt", "r")
input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        if (a, b, c) in wd:
            return wd[(a, b, c)]
        else:
            wd.setdefault((a, b, c), 1)
            return wd[(a, b, c)]
    if a > 20 or b > 20 or c > 20:
        if (a, b, c) in wd:
            return wd[(a, b, c)]
        else:
            wd.setdefault((a, b, c), w(20, 20, 20))
            return wd[(a, b, c)]
    if a < b < c:
        if (a, b, c) in wd:
            return wd[(a, b, c)]
        else:
            wd.setdefault((a, b, c), w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c))
            return wd[(a, b, c)]
    else:
        if (a, b, c) in wd:
            return wd[(a, b, c)]
        else:
            wd.setdefault((a, b, c), w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1))
            return wd[(a, b, c)]


wd = {}
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f"w{a, b, c} =", w(a, b, c))
