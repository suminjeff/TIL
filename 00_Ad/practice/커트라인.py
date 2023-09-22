import sys
sys.stdin = open("커트라인.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[K-1])