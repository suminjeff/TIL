import sys
sys.stdin = open('Z.txt', 'r')
input = sys.stdin.readline

# 1. 일반화를 해야할 것 같지만 일단 분할정복을 해본다


def divide(depth, start_r, end_r, start_c, end_c):
    global cnt
    middle_r, middle_c = (start_r+end_r)//2, (start_c+end_c)//2
    if start_r <= r < middle_r and start_c <= c < middle_c:
        end_r, end_c = middle_r, middle_c
        arr[depth] = 0
    elif start_r <= r < middle_r and middle_c <= c < end_c:
        end_r, start_c = middle_r, middle_c
        arr[depth] = 1
    elif middle_r <= r < end_r and start_c <= c < middle_c:
        start_r, end_c = middle_r, middle_c
        arr[depth] = 2
    elif middle_r <= r < end_r and middle_c <= c < end_c:
        start_r, start_c = middle_r, middle_c
        arr[depth] = 3
    if depth == 0:
        return
    divide(depth-1, start_r, end_r, start_c, end_c)


N, r, c = map(int, input().split())
arr = [0]*N
cnt = 0
n = 2**N
divide(N-1, 0, n, 0, n)
ans = 0
for i in range(N):
    ans += arr[i]*(2**i)**2
print(ans)