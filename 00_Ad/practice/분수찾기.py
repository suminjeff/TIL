import sys

sys.stdin = open("분수찾기.txt", "r")

X = int(input())

min_n = 1

r = c = 1

sr = [0, 1]
sc = [1, 0]
si = 0

xr = [1, -1]
xc = [-1, 1]
xi = 0

cnt = 1

ans = f"{r}/{c}"

while cnt != X:
    r, c = r + sr[si], c + sc[si]
    si = (si + 1) % 2
    cnt += 1
    if cnt == X:
        ans = f"{r}/{c}"
        break
    else:
        while True:
            if r + xr[xi] >= 1 and c + xc[xi] >= 1:
                r, c = r + xr[xi], c + xc[xi]
                cnt += 1
                if cnt == X:
                    ans = f"{r}/{c}"
                    break
            else:
                xi = (xi+1) % 2
                break
print(ans)
