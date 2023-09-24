import sys
sys.stdin = open("풍선 터뜨리기.txt", "r")
input = sys.stdin.readline

N = int(input())
cq = list(map(int, input().split()))
visited = [0]*N
i = 0
remaining = N
ans = []
while remaining:
    v = cq[i]
    visited[i] = 1
    ans.append(i+1)
    remaining -= 1
    if remaining == 0:
        break
    if v > 0:
        for _ in range(v):
            i = (i+1) % N
            while visited[i]:
                i = (i + 1) % N
    elif v < 0:
        for _ in range(-v):
            if i == 0:
                i = N-1
            else:
                i -= 1
            while visited[i]:
                if i == 0:
                    i = N-1
                else:
                    i -= 1
print(*ans)