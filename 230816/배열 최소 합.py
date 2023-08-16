import sys

sys.stdin = open("배열 최소 합.txt", "r")


# def permutation(idx, total):
#     global min_total
#     # 종료 조건
#     if idx == N:
#         total = 0
#         for i in range(len(arr)):
#             total += given[i][arr[i]]
#             if min_total < total:
#                 return
#         min_total = total
#     elif total >= min_total:
#         return
#     else:
#         for swap_idx in range(idx, N):  # 바꿀 위치를 반복
#             arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
#             permutation(idx + 1, total + given[idx][arr[idx]])  # 다음 자리 확인
#             arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]  # 원상 복구 (처음 모양에서 자리를 바꾸는게 아니라 바뀌어진 모양에서 또 자리를 바꾸기 때문에 결과를 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)


def permutation(idx, total):
    # 종료 조건
    global min_total

    if idx == N:
        if min_total <= total:
            return
        min_total = total
    else:
        for swap_idx in range(idx, N):  # 바꿀 위치를 반복
            arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
            permutation(idx + 1, total + given[idx][arr[idx]])  # 다음 자리 확인
            # print(arr)
            arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]  # 원상 복구 (처음 모양에서 자리를 바꾸는게 아니라 바뀌어진 모양에서 또 자리를 바꾸기 때문에 결과를 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)


# permutation(0)
# print(per)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    given = [list(map(int, input().split())) for _ in range(N)]
    arr = [n for n in range(N)]

    min_total = 90
    permutation(0)

    print(f"#{tc} {min_total}")

