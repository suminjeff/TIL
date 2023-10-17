import sys
sys.stdin = open("멀티탭 스케쥴링.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
electronics = list(map(int, input().split()))
counts = [101]*(K+1)
multi_tab = [0]*N
for e in electronics:
    if counts[e] == 101:
        counts[e] = 1
    else:
        counts[e] += 1

for i in range(1, K+1):
    e = electronics[i]
    for j in range(N):
        if multi_tab[j] == 0:
            multi_tab[j] = e
            counts[e] -= 1
            break
        else:
            using = multi_tab[j]

print(counts)

