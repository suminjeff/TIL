N = int(input())
arr = [list(input()) for _ in range(N)]


def candy_check(arr):
    # 행, 열 비교 후 둘 중 제일 큰 값
    max_row_col = 1
    # 행 방향 체크
    row_max = 1
    for r in range(N):
        count = 1
        temp_count = 1
        for c in range(N-1):
            if arr[r][c] == arr[r][c+1]:
                count += 1
            else:
                count, temp_count = 1, count
            # 행 내 최댓값 갱신
            if count < temp_count:
                count = temp_count
        # 전체 배열 내 최댓값 갱신(행 방향만)
        if row_max < count:
            row_max = count

    # 열 방향 체크
    col_max = 1
    for c in range(N):
        count = 1
        temp_count = 1
        for r in range(N-1):
            if arr[r][c] == arr[r+1][c]:
                count += 1
            else:
                count, temp_count = 1, count
            # 행 내 최댓값 갱신
            if count < temp_count:
                count = temp_count
        # 전체 배열 내 최댓값 갱신(열 방향만)
        if col_max < count:
            col_max = count

    # col_max, row_max 중 제일 큰 거
    for num in [col_max, row_max]:
        if max_row_col < num:
            max_row_col = num

    return max_row_col


# 배열을 돌면서 오른쪽(혹은 아래쪽)과 다르면
# 교환 후 case_max = check_candy(arr) 하고
# 교환은 오른쪽이랑 아래만 보면 됨(인덱스 내에서)
# result_max 비교 후 갱신
result_max = 1
for row in range(N):
    for col in range(N):
        # 행 내에서 열(좌우) 바꾸기
        if col+1 < N and arr[row][col] != arr[row][col+1]:
            arr[row][col], arr[row][col+1] = arr[row][col+1], arr[row][col]
            case_max = candy_check(arr)
            if result_max < case_max:
                result_max = case_max
            #원위치
            arr[row][col], arr[row][col+1] = arr[row][col+1], arr[row][col]

        # 열 내에서 행(상하) 바꾸기
        if col+1 < N and arr[col][row] != arr[col+1][row]:
            arr[col][row], arr[col+1][row] = arr[col+1][row], arr[col][row]
            case_max = candy_check(arr)
            if result_max < case_max:
                result_max = case_max
            # 원위치
            arr[col][row], arr[col+1][row] = arr[col+1][row], arr[col][row]

print(result_max)