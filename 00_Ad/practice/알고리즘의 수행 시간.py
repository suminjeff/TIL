import sys
sys.stdin = open("알고리즘의 수행 시간.txt", "r")

n = int(input())
print(n * (n-1) * (n-2) // 6)
print(3)