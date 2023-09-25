import sys
sys.stdin = open("녹색거탑.txt", "r")
input = sys.stdin.readline

N = int(input())
print(2**N)