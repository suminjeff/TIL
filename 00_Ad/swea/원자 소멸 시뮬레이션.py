import sys
import time

start_time = time.time()

sys.stdin = open("원자 소멸 시뮬레이션.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atom = [[] for _ in range(4)]
    # 상(0), 하(1), 좌(2), 우(3)
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom[direction].append([x, y, energy])
    up, down, left, right = atom

    for i in range(0, 4, 2):




    print(f"#{tc}")

end_time = time.time()
print(f"time :", end_time-start_time)