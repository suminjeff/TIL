# 별이 두 개일 때
# dictionary의 값만 풀어서 전달할 때
# 함수를 정의할 때는 dictionary 형으로 묶어준다.

def my_func2(**kargs):
    print(kargs)

my_func2(apple='맛있어', banana='노란색', coconut='지코')

my_dict = {
    'apple' : '맛있어',
    'banana' : '노란색',
    'coconut' : '달콤해',
}

# 딕셔너리의 key : value를 keyword 인자 형태로 전달
#(함수의 매개변수가 가변 키워드 인자이기 때문에)
my_func2(**my_dict)

def my_func3(apple, banana, coconut):
    print(apple, banana, coconut)

# 위치 인자로 키워드 인자를 받으려면 매개변수에 신경을 써야한다
# 딕셔너리를 언패킹 할 때
# 딕셔너리의 키 이름과 매개변수명이 같은지를 확인하자

my_func3(**my_dict)