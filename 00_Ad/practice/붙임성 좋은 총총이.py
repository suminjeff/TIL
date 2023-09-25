import sys
sys.stdin = open("붙임성 좋은 총총이.txt", "r")
input = sys.stdin.readline


key = "Chong Chong"


people = {}
N = int(input())
flag = False
for _ in range(N):
    A, B = input().split()
    if A == key or B == key:
        
    else:
        if A not in people:
            people.setdefault(A, 0)
        if B not in people:
            people.setdefault(B, 0)
