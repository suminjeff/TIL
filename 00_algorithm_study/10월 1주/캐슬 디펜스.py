import sys
sys.stdin = open("캐슬 디펜스.txt", "r")
input = sys.stdin.readline


def nCr(n, r, res):
    if n == len(position):
        if len(res) == r:
            print(res)
        return
    res.append(position[n])
    nCr(n+1, r, res)
    res.pop()
    nCr(n+1, r, res)


def shoot(archer_position):
    a1, a2, a3 = archer_position
    killed = [[0]*N for _ in range(M)]
    wave = N-1


N, M, D = map(int, input().split())
# enemy = [[] for _ in range(M)]
# for n in range(N):
#     row = list(map(int, input().split()))
#     for m in range(M):
#         enemy[m].append(row[m])

enemy = [list(map(int, input().split())) for _ in range(N)]
print(enemy)
position = [m for m in range(M)]
archers = [0] * 3
nCr(0, 3, [])