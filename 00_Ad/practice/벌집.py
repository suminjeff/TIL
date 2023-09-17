import sys

sys.stdin = open("벌집.txt", "r")

N = int(input())

start = 1
a = 1
end = start + 6 * a

if N == 1:
    print(1)

else:
    while not start < N <= end:
        start = end
        a += 1
        end = start + 6 * a
    print(a+1)