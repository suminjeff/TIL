def permutation(idx):
    if idx == N:
        print(*arr)
        return
    for swap_idx in range(idx, N): # 바꿀 위치를 반복
        arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
        permutation(idx + 1) # 다음 자리 확인
        arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx] # 원상 복구 (처음 모양에서 자리를 바꾸는 게 아니라 바뀐 모양에서 또 자리를 바꾸기 때문에 결과를 예측하기 어려워지고 잘못된 동작을 수행하게 됨.


N, M = map(int, input().split())

arr = [n for n in range(1, N+1)]

idx = 0
permutation(idx)