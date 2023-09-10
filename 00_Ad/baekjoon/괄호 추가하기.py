import sys

sys.stdin = open("괄호 추가하기.txt", "r")

N = int(input())
phrase = input()
max_brackets = (N//2+1)//2

print(phrase)