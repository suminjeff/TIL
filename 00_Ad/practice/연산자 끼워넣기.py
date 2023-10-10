import sys
sys.stdin = open('연산자 끼워넣기.txt', 'r')
input = sys.stdin.readline


def backtrack(idx, res, track):
    global max_res, min_res
    if idx == N-1:
        max_res, min_res = max(max_res, res), min(min_res, res)
        return
    idx += 1
    for i in range(4):
        if ops[i]:
            if i == 0:
                new_res = res + A[idx]
            elif i == 1:
                new_res = res - A[idx]
            elif i == 2:
                new_res = res * A[idx]
            else:
                if res < 0:
                    new_res = -(-res // A[idx])
                else:
                    new_res = res // A[idx]
            track.append(i)
            ops[i] -= 1
            backtrack(idx, new_res, track)
            track.pop()
            ops[i] += 1


N = int(input())
A = list(map(int, input().split()))
# 0: +, 1: -, 2: *, 3: /
ops = list(map(int, input().split()))

max_res = float('-inf')
min_res = float('inf')
backtrack(0, A[0], [])
print(max_res)
print(min_res)