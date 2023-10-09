import sys
sys.stdin = open("색종이 붙이기.txt", "r")
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(10)]