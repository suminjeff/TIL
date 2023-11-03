import sys
sys.stdin = open('테트로미노2.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]