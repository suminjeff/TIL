import sys

sys.stdin = open("불면증.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = input()
    nums = set()
    cnt = 0
    n = 1
    while len(nums) < 10:
        num = str(int(N)*n)
        for i in num:
            nums.add(i)
        cnt += 1
        n += 1
    ans = int(N)*cnt
    print(f"#{tc} {ans}")