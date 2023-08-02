import sys
sys.stdin = open("어디에 단어가 들어갈 수 있을까.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # 행 탐색
    for row in range(N):
        space = 0
        for col in range(N):
            if arr[row][col] == 1:
                space += 1
            if arr[row][col] == 0 or col == N-1:
                if space == K:
                    count += 1
                if arr[row][col] == 0:
                    space = 0
                    
    # 열 탐색
    for col in range(N):
        space = 0
        for row in range(N):
            if arr[row][col] == 1:
                space += 1
            if arr[row][col] == 0 or row == N-1:
                if space == K:
                    count += 1
                if arr[row][col] == 0:
                    space = 0

    print(f"#{tc} {count}")