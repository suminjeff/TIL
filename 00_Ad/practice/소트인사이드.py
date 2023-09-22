import sys
sys.stdin = open("소트인사이드.txt", "r")
input = sys.stdin.readline

arr = list(input())
arr.sort(reverse=True)
print(*arr, sep="")