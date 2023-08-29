coin_type = [500, 100, 50, 10]

# 받은 돈
N = 1260
ans = 0
for coin in coin_type:
    while N//coin != 0:
        ans += N//coin
        N = N % coin

# 거스름돈의 개수
print(ans)