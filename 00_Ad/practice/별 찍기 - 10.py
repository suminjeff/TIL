import sys
sys.stdin = open("별 찍기 - 10.txt", "r")
input = sys.stdin.readline


def func(n):
    if n == 1:
        return ['*']
    star = func(n//3)
    res = []

    for s in star:
        res.append(s*3)
    for s in star:
        res.append(s+" "*(n//3)+s)
    for s in star:
        res.append(s*3)
    return res


N = int(input())
print("\n".join(func(N)))