import sys

sys.stdin = open("정곤이의 단조 증가하는 수.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            num_str = str(num)
            isIncrease = True
            for k in range(len(num_str) - 1):
                if int(num_str[k]) > int(num_str[k + 1]):
                    isIncrease = False
            if isIncrease:
                max_v = max(max_v, num)

    print(f"#{tc} {max_v}")

