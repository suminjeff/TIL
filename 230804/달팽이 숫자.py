import sys
sys.stdin = open("달팽이 숫자.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    count = 1
    for row in range(N):
        for col in range(N):
            arr[row][col] += count
            count += 1
            for k in range(4):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0 <= 


    print(f"#{tc}")
    for n in range(N):
        print(*arr[n])