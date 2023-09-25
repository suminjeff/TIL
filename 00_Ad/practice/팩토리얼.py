import sys
sys.stdin = open("팩토리얼.txt", "r")
input = sys.stdin.readline


def factorial(num):
    ans = 1
    for i in range(2, num+1):
        ans *= i
    return ans

N = int(input())
print(factorial(N))