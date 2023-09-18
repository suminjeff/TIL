import sys

sys.stdin = open("소수.txt", "r")

M = int(input())
N = int(input())
res = []
for num in range(M, N+1):
    if num == 1:
        continue
    else:
        tmp = []
        for n in range(2, num):
            if num % n == 0:
                tmp.append(n)
                break
        if not tmp:
            res.append(num)
if sum(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))