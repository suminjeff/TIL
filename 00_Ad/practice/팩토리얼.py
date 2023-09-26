import sys
sys.stdin = open("팩토리얼.txt", "r")
input = sys.stdin.readline


def factorial(num):
    ans = 1
    for i in range(2, num+1):
        ans *= i
    return ans


def factorial2(num):
    if num == 1:
        return 1
    return num * factorial(num-1)



N = int(input())
print(factorial(N))