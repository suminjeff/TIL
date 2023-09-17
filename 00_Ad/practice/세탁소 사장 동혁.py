import sys

sys.stdin = open("세탁소 사장 동혁.txt", "r")

coins = [25, 10, 5, 1]

T = int(input())
for tc in range(1, T+1):
    total = int(input())
    ans = []
    for coin in coins:
        ans.append(total//coin)
        total %= coin
    print(*ans)