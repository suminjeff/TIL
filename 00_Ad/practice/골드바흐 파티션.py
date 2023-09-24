import sys
sys.stdin = open("골드바흐 파티션.txt", "r")
input = sys.stdin.readline


primes = [


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f"#{tc}")