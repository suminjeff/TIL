import sys
sys.stdin = open("원자 소멸 시뮬레이션.txt", "r")

direction = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    que = [list(map(int, input().split())) for _ in range(N)]
    mx = my = 1000
    MX = MY = -1000
    for i in range(N):
        p, q = que[i][0], que[i][1]
        mx, my = min(mx, p), min(my, q)
        MX, MY = max(MX, p), max(MY, q)

    ans = 0
    while que:
        boom = set()
        energy = {}
        for turn in range(len(que)):
            x, y, d, e = que.pop(0)
            dx, dy = direction[d]
            x, y = x+dx, y+dy
            if mx <= x <= MX and my <= y <= MY:
                if (x, y) in energy.keys():
                    energy[(x, y)][1] += e
                    boom.add((x, y))
                else:
                    energy.setdefault((x, y), [d, e])
        if boom:
            for nx, ny in energy.keys():
                d, ne = energy[(nx, ny)][0], energy[(nx, ny)][1]
                if (nx, ny) in boom:
                    ans += ne
                else:
                    que.append([nx, ny, d, ne])
        else:
            for nx, ny in energy.keys():
                d, ne = energy[(nx, ny)][0], energy[(nx, ny)][1]
                que.append([nx, ny, d, ne])

    print(f"#{tc} {ans}")