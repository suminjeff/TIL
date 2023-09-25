import sys
sys.stdin = open("창문 닫기.txt", "r")
input = sys.stdin.readline

N = int(input())
print(int(N**0.5))