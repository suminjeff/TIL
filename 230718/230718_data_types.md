# 데이터 타입 (Data Types)

1. Data Types
    - 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
    - 데이터 타입이 필요한 이유
        - 값들을 구분하고, 어떻게 다뤄야 하는지 알 수 있음
        - 타입마다 각자에게 적합한 도구를 가짐
        - 타입을 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해 가능
        - 잘못된 데이터 타입으로 인한 오류를 예방

2. 수치형 Numeric Types
    - 정수형 (int)
        - 정수를 표현
        - 진수 표현도 포함
            - 2진수 binary 0b
            - 8진수 octal 0o
            - 16진수 hexadecimal 0x
    - 실수형 (float)
        - 유리수와 무리수
        - 프로그래밍 언어에서 float는 실수에 대한 근삿값
            - 유한 정밀도
                - 컴퓨터 메모리 용량이 한정되어 한 숫자에 대해 저장하는 용량이 제한됨
                - **그래서 실수 연산 시 주의해야 함**
                    - Floating point rounding error (부동 소수점 라운딩 에러)
                    - 해결책
                        - 두 수의 차이가 매우 작은 수보다 작은지를 확인하거나 math 모듈 사용
        - 지수 표현 방식
            - e 또는 E를 사용한 지수 표현
            - 314 * 0.01
                - number = 314e-2
    - 복소수 (complex)

3. Sequence Type
    - 여러 개의 값들을 **순서대로 나열**해 저장하는 자료형
    - 특징
        - 순서 (sequence)
            - 값들이 순서대로 저장되어 있음 (정렬은 아님)
        - 인덱싱 (indexing)
            - 각 값에 고유한 인덱스가 있음. 이를 활용해 특정 위치의 값을 선택/수정할 수 있음
        - 슬라이싱 (slicing)
            - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
        - 길이 (length)
            - len() 함수를 사용해 저장된 값의 개수(길이)를 구할 수 있음
        - 반복 (iteration)
            - 반복문을 사용해 저장된 값들을 반복적으로 처리할 수 있음
    - str
        - 문자들의 순서가 있는 **변경 불가**한 시퀀스 자료형 (불변형)
            - 접근은 가능하지만 할당은 안됨
            - 바꾸지 말고 새로운 문자열을 만들어야함
        - pep8 style guide에 따르면 따옴표 스타일 하나만 쓸 것
        - 따옴표 안에 따옴표를 쓰려면 escape sequence('\') 쓰거나 다른 따옴표를 써야 함
        - String Interpolation
            - 문자열 내에 변수나 표현식을 삽입하는 방법
            - 문자열에 f/F 접두어를 붙이고 표현식을 {expression}로 작성해 문자열에 파이썬 값을 삽입할 수 있음 (f-string advanced)
        - 인덱싱[1], 슬라이싱[0:5:2], 길이(len())를 구할 수 있음
            - 슬라이싱
                - 파이썬의 독특한 문자열 뒤집기 [::-1]
    - list
        - 여러 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형 (가변형)
        - 0개 이상의 객체를 포함하며 데이터 목록을 저장
        - 대괄호로 표기
        - 데이터는 어떤 자료형도 저장 가능 (중첩 리스트)
    - tuple
        - 여러 값을 순서대로 저장하는 변경 불가한 시퀀스 자료형 (불변형)
        - 0개 이상의 객체를 포함하며 데이터 목록을 저장
        - 소괄호로 표기
        - 데이터는 어떤 자료형도 저장 가능 (중첩 리스트)
        - (1,) (1)은 그냥 int이므로 tuple로 인식되게 하기 위해 (1,)라고 씀
        - 튜플의 목적
            - 개발자가 직접 사용하기보다는 파이썬이 내부적인 동작을 위해 쓰는 타입
            - 값이 바뀌지 않으니깐 안정적
            - 파이썬은 쉼표를 튜플 생성자로 사용해 괄호 생략 가능
                - x, y = 10, 20
    - range
        - 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
        - range(n) : 0부터 n-1까지의 숫자 시퀀스
        - range(n, m) : n부터 m-1까지의 숫자 시퀀스
        - 리스트로 형 변환
            - list(range(n, m))

4. Non-sequence Types
    - dict
        - key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형 (가변형)
        - key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range, 등)
        - value는 모든 자료형 사용 가능
        - 중괄호({})로 표기
        - key를 통해 value에 접근
    - set
        - 순서와 중복이 없는 변경 가능한 자료형
        - 수학에서의 집합과 동일한 연산 처리 가능
        - 중괄호로 표기
        - set()로 빈 세트 생성
        - 중복이 없음
            - {1, 1, 1} -> {1}
        - 순서가 없음
            - 인덱스x, 슬라이싱x
        - 합집합(|), 차집합(-), 교집합(&)
5. Other Types
    - None
        - 값이 없음을 표현하는 자료형
    - Boolean
        - 참과 거짓을 표현하는 자료형
        - 비교/논리 연산의 평가 결과로 사용됨
        - 주로 조건/반복문과 함께 사용

6. Collection
    - 여러 개의 항목 또는 요소를 담는 자료구조
        - str, list, tuple, set, dict
    

7. Type Conversion
    - 암시적 형변환 (드러나지 않는다)
        - 파이썬이 자동으로 형변환을 해준다(필요할 때)
            - Boolean과 Numeric Type에서만 가능 (더 넓은 값의 범위를 표현)
                - 정수 + 실수 = 실수
                - 불리언 + 정수 = 정수
                - 불리언 + 불리언 = 정수
                - if문에서 판단할때만 형변환
                - 0, '', [], (), {} 모두 False

    - 명시적 형변환 (개발자가 직접 형변환)                
        - str -> integer : 형식에 맞는 숫자만 가능
        - integer -> str : 모두 가능

8. 연산자