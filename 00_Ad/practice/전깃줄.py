import sys
sys.stdin = open("전깃줄.txt", "r")
input = sys.stdin.readline

N = int(input())
wire = [0]*501
max_s = 0
max_e = 0
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(min(s, e), max(s, e)+1):
        wire[i] += 1
    # print(wire)
    # wire[s] = e
    if max_s < s:
        max_s = s
    if max_e < e:
        max_e = e
print(wire)
print(max(wire)-1)

