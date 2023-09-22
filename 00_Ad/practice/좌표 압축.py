import sys
sys.stdin = open("좌표 압축.txt", "r")
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
Xset = sorted(list(set(X)))
Xdic = {x:Xset.index(x) for x in Xset}
for i in range(N):
    print(Xdic[X[i]], end=" ")