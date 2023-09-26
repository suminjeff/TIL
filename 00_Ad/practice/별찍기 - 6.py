import sys
sys.stdin = open("별찍기 - 6.txt", "r")
input = sys.stdin.readline

def star(n):
    for i in range(n, 0, -1):
        print((' ' * (n-i)) + ('*' * (2*i-1)))

N = int(input())
star(N)