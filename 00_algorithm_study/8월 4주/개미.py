import sys
import time

sys.stdin = open("개미.txt", "r")
start_time = time.time()

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((p+t)//w) % 2 == 0:
    x = (p+t) % w
elif ((p+t)//w) % 2 == 1:
    x = w - ((p+t) % w)

if ((q+t)//h) % 2 == 0:
    y = (q+t) % h
elif ((q+t)//h) % 2 == 1:
    y = h - ((q+t) % h)


# 시간초과 코드
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x_increase = 1
y_increase = 1

for i in range(t):
    if p == w:
        x_increase = -1
    elif p == 0:
        x_increase = 1
    if q == h:
        y_increase = -1
    elif q == 0:
        y_increase = 1
    p += x_increase
    q += y_increase

print(p, q)


print(x, y)
end_time = time.time()
print("time: ", end_time - start_time)
