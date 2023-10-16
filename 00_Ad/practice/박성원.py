import sys
sys.stdin = open("박성원.txt", "r")
input = sys.stdin.readline


def perm(depth, string):
    global p, q
    if depth == N:
        q += 1
        if int(string) % K == 0:
            p += 1
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            perm(depth+1, string+arr[i])
            used[i] = 0


def gcd(p, q):
    while q > 0:
        p, q = q, p%q
    return p


N = int(input())
arr = [input().rstrip() for _ in range(N)]
used = [0]*N
K = int(input())

p = 0
q = 0

perm(0, "")
d = gcd(p, q)
print(f"{p//d}/{q//d}")