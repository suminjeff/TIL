import sys

sys.stdin = open("스위치 켜고 끄기.txt", "r")

N = int(input())            # 스위치 개수
arr = list(map(int, input().split()))       # 원래의 스위치
student = int(input())      # 학생 수

for k in range(student):
    stu_info = list(map(int, input().split()))

    if stu_info[0] == 1:        # 남학생 스위치 규칙
        for i in range(1, N+1):
            if stu_info[1] * i <= N:                    # 입력받은 숫자의 배수 부분을 스위칭한다.

                if arr[(stu_info[1] * i) - 1] == 1:     # 0이면 1로 1이면 0으로
                    arr[(stu_info[1] * i) - 1] = 0
                else:
                    arr[(stu_info[1] * i) - 1] = 1

    elif stu_info[0] == 2:                # 여학생 스위치 규칙

        if arr[stu_info[1]-1] == 0:       # 일단 입력값 부분은 무조건 바꾸니까 0이면 1로 1이면 0으로
            arr[stu_info[1]-1] = 1
        else:
            arr[stu_info[1]-1] = 0

        for j in range(1, N):
            if 0 <= (stu_info[1]-1-j) and (stu_info[1]-1+j) < N:
               if arr[stu_info[1]-1-j] == arr[stu_info[1]-1+j]:
                   # 입력값 부분의 양쪽이 같다면 걔내도 바꾼다.

                   if arr[stu_info[1]-1-j] == 0:        # 0이면 1로 1이면 0으로
                       arr[stu_info[1]-1-j] = 1
                   else:
                       arr[stu_info[1]-1-j] = 0

                   if arr[stu_info[1]-1+j] == 0:        # 0이면 1로 1이면 0으로
                       arr[stu_info[1]-1+j] = 1
                   else:
                       arr[stu_info[1]-1+j] = 0
               else:
                   break

# num = len(arr) // 20                # 20개 이상 스위치를 입력받으면 20개로 끊어서 출력하라고
# remain = len(arr) % 20              # 해서 만들었습니다.
# if num >= 1:
#     for i in range(num):
#         print(*arr[20*i:(20*i)+20])
#     print(*arr[-remain:])
# else:
#     print(*arr)

for i in range(N):
    print(arr[i], end=" ")
    if i % 20 == 19:
        print()