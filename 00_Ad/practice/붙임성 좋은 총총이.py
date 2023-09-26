import sys
sys.stdin = open("붙임성 좋은 총총이.txt", "r")
input = sys.stdin.readline


key = "ChongChong"

people = set()
N = int(input())
for _ in range(N):
    A, B = input().split()
    if A == key or B == key:
        people.add(A)
        people.add(B)
    elif A in people or B in people:
        people.add(A)
        people.add(B)
print(len(people))