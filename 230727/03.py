try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100/num)
except ValueError:
    print('숫자를 입력하세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생했어')