# 함수
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
- 사용하는 이유
    - 코드의 중복 방지
    - 재사용성 향상, 가독성과 유지보수성 향상

## 내장 함수 (Built-in function)
- 파이썬이 기본적으로 제공하는 함수 (import 없이 바로 사용 가능)
- 예시
    - abs (절댓값을 만드는 함수)
        - `result = abs(-1)`
        - `print(result)`
- 내장 함수 리스트는 파이썬 공식문서에서 (python documentation)
- 구조
    - input : (def function(parameter)) 매개변수
    - body : Docstring, function body
    - output : (return) 반환값 (필요한 경우. 반환값 없는 함수도 있음). 반환값 설정을 안하면 함수의 반환값이 None이 됨
- 매개변수와 인자(argument)
    - 매개변수
        - 함수를 정의할 때 함수가 받을 값을 나타내는 변수 (동물)
    - 인자
        - 함수를 호출할 때, 실제로 전달되는 값 (기린)
        - 위치인자(Positional Arguments)
            - 함수 호출 시 인자의 위치에 따라 전달되는 인자
            - 위치인자는 함수 오출 시 반드시 값을 전달해야 함
        - 기본 인자 값(Default Argument Values)
            - 함수 정의에서 매개변수에 기본 값을 할당하는 것
            - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
        - 키워드 인자(Keyword Arguments)
            - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
            - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
            - 인자의 순서는 중요치 않고, 인자의 이름을 명시해 전달
            - 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함
        - 임의의 인자 목록(Arbitrary Argument Lists)
            - 정해지지 않은 개수의 인자를 처리하는 인자
            - 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
        - 임의의 키워드 인자 목록(Arbitrary Keyword Argument Lists)
            - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
            - 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리
        - 함수 인자 권장 작성 순서
            - 위치 -> 기본 -> 가변 -> 가변 키워드

## 함수와 Scope(공간)
- Python의 범위
    - 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
    - Scope
        - Global scope : 코드 어디에서든 참조할 수 있는 공간
        - Local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)
        - Scope 예시
            - num은 local scope에 존재하기 때문에 global에서 사용할 수 없음
            - 이는 변수의 수명주기와 연관이 있음
                - 변수의 수명주기(Lifecycle)  
                    1. built-in scope
                        - 파이썬이 실행된 이후부터 영원히 유지
                    1. global scope
                        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
                    1. local scope
                        - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    - Variable
        - Global variable : Global scope에 정의된 변수
        - Local variable : Local scope에 정의된 변수

    - 이름 검색 규칙(Name Resolution)
        - 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
        - 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
            1. Local scope : 지역 범위
            1. Enclosed scope : 지역 범위 한 단계 위 범위
            1. Global scope : 최상단에 위치한 범위
            1. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
        - 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정할 수 없음
        - 그러나 된다고 해서 이렇게 함수를 정의하고 코드를 짜는 것은 좋지 않음
    - global 키워드
        - 변수의 스코프를 전역 범위로 지정하기 위해 사용
        - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

## 재귀 함수
- 함수 내부에서 자기 자신을 호출하는 함수
- 특징
    - 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
    - 1개 이상의 base case(종료되는 상황)기 존재하고, 수렴하도록 작성
- 재귀함수 예시 - 팩토리얼
- 재귀 함수 제한
    import sys
    dir sys # 사용할 수 있는 함수 모음
    getrecursionlimit # 제한 확인
    setrecursionlimit # 
    sys.getrecursionlimit() # 1000
    sys.setrecursionlimit(5000)
    sys.getrecursionlimit() # 5000

## 유용한 함수

### 유용한 내장함수
- map(function, iterable)
    - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

- zip(*iterables)
    - 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

- lambda 매개변수: 표현식 (이름 없이 정의되고 사용되는 익명 함수)
    - 간단한 연산이나 함수를 한 줄로 표현할 때 사용
    - 함수를 매개변수로 전달하는 경우에도 유용하게 사용
    - lambda 키워드
        - 람다 함수를 선언하기 위해 사용되는 키워드
    
## Packing & Unpacking

### Packing
- 여러 개의 값을 하나의 변수에 묶어서 담는 것
- 변수에 담긴 값들은 튜플(tuple) 형태로 묶임 (값에 ,만 넣어주면 pyton이 알아서 tuple로 묶어줌)
- *를 활용한 패킹
    - `numbers = [1, 2, 3, 4, 5]`
    - `a, *b, c = numbers`
    - `print(a)` # 1
    - `print(b)` # [2, 3, 4]
    - `print(c)` # 5
- 따지고 보면 print() 함수의 가변인자도 패킹을 활용한 것
- 정의할 땐 Packing (가변인자)
    - `def my_func(*args):`
    - `print(args)`
    - `my_func('a', 'b', 'c')` # ('a', 'b', 'c')

### Unpacking
- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
    - `packed_values = 1, 2, 3, 4, 5`
    - `a, b, c, d, e = packed values`
    - `print(a, b, c, d, e)` # 1 2 3 4 5
- *를 활용한 언패킹
    - *는 리스트의 요소를 언패킹
- 호출할 땐 Unpacking
    - `my_func(my_list)` # list 채로 값이 전달됨 (unpacking 아님)
    - `my_func(*my_list)` # list의 값이 unpacking 돼서 전달됨
- **를 활용한 언패킹
    - **는 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹해서 값들이 전달됨
    - dictionary의 값만 풀어서 전달할 때 쓰임 (함수 호출할 때)

### */** 패킹/언패킹 연산자 정리
- *
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶는 역할
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달

- **
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹하여 함수의 인자로 전달하는 역할

## 모듈
- 누군가 만들어둔 코드를 쓰는 것
- 변수와 함수들을 모은 코드가 작성된 파이썬 파일
- import 모듈명
- from 절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import할지 명시
    - from math import pi, sqrt
- 모듈명.함수()/변수/클래스

## 패키지
- 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것
- PSL 내부 패키지
    - 설치 없이 바로 import해서 사용
- 외부 패키지
    - pip를 사용해 설치 후 import 필요
        - pip는 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
        - PyPI에 저장된 외부 패키지들을 설치 [PyPI](https://pypi.org)
    - 패키지 설치
        - 최신 버전 `pip install SomePackage`
        - 특정 버전 `pip install SomePackage==1.0.5`
        - 최소 버전 `pip install SomePackage>=1.0.4`
    - requests 외부 패키지 설치 및 사용 예시
        - `pip install requests`
        - `import requests`
        - `url = 'https://random-data-api.com/api/v2/users'`
        - `response = requests.get(url).json()`
        - `print(response)`
    - 패키지 사용 목적
        - 모듈들의 이름공간은 구분하여 충돌을 방지
        - 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할


