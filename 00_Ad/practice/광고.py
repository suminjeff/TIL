import sys
sys.stdin = open("광고.txt", "r")
input = sys.stdin.readline

N = int(input())
string = input()

cq = [0] * 1000001
front = rear = -1

