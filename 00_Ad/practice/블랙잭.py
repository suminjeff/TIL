import sys
sys.stdin = open("블랙잭.txt", "r")

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
min_diff = float("inf")

