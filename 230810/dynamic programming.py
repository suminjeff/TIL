def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    

def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        global cnt2
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]

    return f[n]


def fibo3(n):
    global cnt3
    global memo
    cnt3 += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]


n = 30

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

cnt = 0
cnt2 = 0
cnt3 = 0

print(fibo(n), cnt)
print(fibo2(n), cnt2)
print(fibo3(n), cnt3)