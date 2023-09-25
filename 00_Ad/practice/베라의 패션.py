import sys
sys.stdin = open("베라의 패션.txt", "r")
input = sys.stdin.readline

N = int(input())
print(N*(N-1))