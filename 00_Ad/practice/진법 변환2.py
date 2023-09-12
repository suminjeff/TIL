import sys

sys.stdin = open("진법 변환2.txt", "r")

N, B = map(int, input().split())

ans = ""
while N:
    N, mod = divmod(N, B)
    if mod < 10:
        ans += str(mod)
    else:
        ans += chr(mod + 55)

print(ans)
