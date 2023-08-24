import sys

sys.stdin = open("경비원.txt", "r")

# 블록의 가로 세로
w, h = map(int, input().split())
# 상점의 개수
N = int(input())
# 상점의 위치
arr = [list(map(int, input().split())) for _ in range(N)]
# 동근이의 위치
direction, coordinate = map(int, input().split())
p = q = 0
if direction == 1 or direction == 2:
    p = coordinate
    if direction == 1:
        q = h
elif direction == 3 or direction == 4:
    q = h - coordinate
    if direction == 4:
        p = w

ans = 0
for store in arr:
    # 좌표 구하기
    loc, coor = store[0], store[1]
    x, y = 0, 0
    if loc == 1 or loc == 2:
        x = coor
        if loc == 1:
            y = h
    elif loc == 3 or loc == 4:
        y = h - coor
        if loc == 4:
            x = w
    # 이동거리
    if p == x or q == y:
        if p == x:
            ans += abs(q-y)
        else:
            ans += abs(p-x)
    else:
        # 서로 반대편에 있다면
        if abs(p-x) == w or abs(q-y) == h:
            if abs(p-x) == w:
                case1 = w + h-q + h-y
                case2 = w + q + y
                ans += min(case1, case2)
            else:
                case1 = h + p + x
                case2 = h + w-p + w-x
                ans += min(case1, case2)
        # ㄱ, ㄴ자로 배치되어 있다면
        else:
            ans += abs(p-x) + abs(q-y)
            # if p == 0:
            #     if y == 0:
            #         ans += q + x
            #     elif y == h:
            #         ans += h-q + x
            # elif q == 0:
            #     if x == 0:
            #         ans += p + y
            #     elif x == w:
            #         ans += w-p + y
            # elif p == w:
            #     if y == 0:
            #         ans += h-q + w-x
            #     elif y == h:
            #         ans += h-q + w-x
            # elif q == h:
            #     if x == 0:
            #         ans += p + h-y
            #     elif x == w:
            #         ans += w-p + h-y

print(ans)