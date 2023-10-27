import sys
sys.stdin = open('프린터 큐.txt', 'r')
input = sys.stdin.readline


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    K = N
    priorities = list(map(int, input().split()))
    order = 1
    counts = [0]*10
    max_p = 0
    for p in priorities:
        counts[p] += 1
        max_p = max(max_p, p)
    idx = 0
    while N:
        if priorities[idx] == max_p:
            if idx == M:
                print(order)
                break
            else:
                order += 1
                counts[max_p] -= 1
                N -= 1
                idx = (1 + idx) % K
                max_p = 0
                for i in range(9, 0, -1):
                    if counts[i] > 0:
                        max_p = i
                        break
        else:
            idx = (1 + idx) % K

