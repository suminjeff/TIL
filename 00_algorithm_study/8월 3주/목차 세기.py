import sys

sys.stdin = open("목차 세기.txt", "r")

def check(arr):
    N = len(arr)
    vertex = arr.count(1)
    idx = 0
    for v in range(vertex):
        tree = []
        while idx < N-1:






levels = []
for _ in range(int(input())):
    levels.append(int(input()))
vertex = levels.count(1)
print(levels)
print(vertex)
