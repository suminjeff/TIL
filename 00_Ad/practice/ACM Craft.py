import sys
sys.stdin = open('ACM Craft.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    adj_l = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    for _ in range(K):
        s, e = map(int, input().split())
        adj_l[s].append(e)
    W = int(input())


    print(f"#{tc} {adj_l}")
