import sys
sys.stdin = open("수 정렬하기 2.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
print(*arr, sep="\n")