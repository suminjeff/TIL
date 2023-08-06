import sys
sys.stdin = open("달팽이 숫자.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    # 0으로 채워진 N*N 배열 생성
    arr = [[0]*N for _ in range(N)]

    # 델타 탐색 (우 하 좌 상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    # 시작점의 row, col 좌표 설정
    row = 0
    col = 0

    # 초기 델타값 설정 (우)
    delta = 0
    
    # N*N 배열이니 그만큼 반복
    for n in range(1, N*N + 1):
        # 지나가는 배열마다 n으로 값을 초기화
        arr[row][col] = n
        # 그 다음 행선지는 row + 델타값
        row += dr[delta]
        col += dc[delta]

        # 만약 row, col이 배열의 범위를 벗어나거나, 칸에 0이 아닌 숫자가 있다면
        if row < 0 or col < 0 or row >= N or col >= N or arr[row][col] != 0:
            # 한칸 뒤로 와서
            row -= dr[delta]
            col -= dc[delta]
            
            # 델타 값을 변경
            # +1을 4로 나눈 나머지 (delta의 인덱스는 0~3을 계속 반복해야 함)
            delta = (delta + 1) % 4
            
            # 다시 해당 델타값으로 진행
            row += dr[delta]
            col += dc[delta]

    print(f"#{tc}")
    for n in range(N):
        print(*arr[n])
