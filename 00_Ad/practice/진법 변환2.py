import sys

sys.stdin = open("진법 변환2.txt", "r")

N, B = map(int, input().split())
cnt = 0

ans = []
while N:
    div = N % B
    if div > 9:
        div = chr(div + 55)
    else:
        div = str(div)
    ans.append(div)
    N //= B
ans.reverse()
ans = "".join(ans)
print(ans)