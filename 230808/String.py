import sys

sys.stdin = open("String.txt", "r", encoding='utf-8')


def BruteForce(p, t):
    i = 0         # t의 인덱스
    j = 0         # p의 인덱스
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p):
        return i - len(p)
    else:
        return -1


T = 10
for _ in range(1, T+1):
    tc = int(input())
    p = input()
    t = input()
    ans = 0
    for i in range(len(t) - len(p) + 1):
        if t[i:i+len(p)] == p:
            ans += 1
    print(f"#{tc} {ans}")