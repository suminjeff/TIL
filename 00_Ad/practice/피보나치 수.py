import sys
sys.stdin = open("피보나치 수.txt", "r")
input = sys.stdin.readline

N = int(input())
fibo = [0] + [1] + [0] * (N-1)
for i in range(2, N+1):
    fibo[i] = fibo[i-2] + fibo[i-1]
print(fibo[N])