import sys

sys.stdin = open("활주로 건설.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    row_ans = 0
    # 행 방향
    for r in range(N):
        max_v = max(arr[r])
        stack = []
        temp = []
        for c in range(N):
            v = arr[r][c]
            if stack:
                if v == stack[-1]:
                    stack.append(v)
                else:
                    temp.append(stack)
                    stack = [v]
            else:
                stack.append(v)
            if c == N-1:
                temp.append(stack)

        for i in range(len(temp)-1):
            block1, block2 = temp[i], temp[i+1]
            if block1[0] < block2[0]:
                if len(block1) < X:
                    break
            elif block1[0] > block2[0]:
                if len(block2) < X:
                    break





    col_ans = 0
    # 열방향
    for c in range(N):
        max_v = 0
        for row in range(N):
            max_v = max(max_v, arr[row][c])
        checkbox = [n for n in range(max_v)]
        for v in range(1, max_v):
            cnt = 0
            for r in range(N):
                if arr[r][c] == v:
                    cnt += 1
                    if cnt >= X:
                        checkbox[v] = 1
                        break
                else:
                    cnt = 0
        if sum(checkbox) == max_v - 1:
            ans += 1
            col_ans += 1

    print(f"#{tc} {ans}")
    print(f"#{tc} {row_ans} {col_ans}")