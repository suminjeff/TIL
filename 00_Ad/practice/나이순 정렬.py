import sys
sys.stdin = open("나이순 정렬.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = []
for n in range(N):
    age, name = map(str, input().split())
    arr.append([int(age), name])
arr.sort(key=lambda x: x[0])
for age, name in arr:
    print(age, name)