import sys

sys.stdin = open("소수 찾기.txt", "r")

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    if num == 1:
        continue
    else:
        tmp = []
        for n in range(2, num):
            if num % n == 0:
                tmp.append(n)
        if not tmp:
            cnt += 1
print(cnt)