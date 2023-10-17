import sys
sys.stdin = open("외판원 순회.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

