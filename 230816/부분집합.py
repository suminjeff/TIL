import sys

sys.stdin = open("부분집합.txt", "r")


def powerset(idx):  # idx는 현재 숫자, 위치
    # 종료 조건을 만들자
    global cnt

    if idx == len(arr) + 1:  # selected 크기가 len(arr)+1이기 때문
        # 종료 전에 현재 선택된 부분집합을 출력
        total = 0
        for i in range(len(arr) + 1):
            if selected[i] == True:
                total += i
        if total == 10:
            cnt += 1
        return  # 함수 종료

    # 현 위치를 선택했을 경우
    selected[idx] = True
    powerset(idx + 1)  # 다음 자리 선택

    # 현 위치를 선택하지 않았을 경우
    selected[idx] = False
    powerset(idx + 1)  # 다음 자리 선택


T = 1
for tc in range(1, T+1):
    arr = list(map(int, input().split()))  # 부분 집합
    selected = [False] * (len(arr) + 1)  # 해당 숫자가 선택됐는지 여부
    cnt = 0
    powerset(1)

    print(f"#{tc} {cnt}")
