# 재귀 함수

def factorial(num):
    # 종료 조건: n이 0이면 1을 반환
    if num == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
    return num * factorial(num - 1)

result = factorial(5)
print(result)