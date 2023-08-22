# 최소 힙 삽입
data = [3, 7, 9, 2, 1, 5]
N = 6 # 데이터의 길이

heap = [0] * (N+1)      # 0번 인덱스는 사용 X
last_idx = 1            # 가장 마지막 위치 (초기화 root 인덱스)

# heap에다가 넣어 봅시다
for idx in range(N):
    if not heap[last_idx]:   # root 인덱스
        heap[last_idx] = data[idx]
    else:
        last_idx += 1   # 들어갈 인덱스 마지막 위치
        heap[last_idx] = data[idx] # 마지막 위치에 값을 삽입
        # 우선순위 비교를 위한 준비
        parent = last_idx // 2
        child = last_idx

        while heap[parent] > heap[child]:
            # 부모 노드와 자식 노드를 교체
            heap[parent], heap[child] = heap[child], heap[parent]
            # 다음 부모노드와 자식노드를 지정
            child = parent
            parent = child // 2
print(heap)