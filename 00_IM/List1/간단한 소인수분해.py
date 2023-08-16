import sys
sys.stdin = open("간단한 소인수분해.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [2, 3, 5, 7, 11]
    N = int(input())
    ans = []
    for i in arr:
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
        ans.append(cnt)

    print(f"#{tc}", *ans)