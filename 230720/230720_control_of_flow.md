# 제어문
- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

---

## 조건문
- 주어진 조건식을 평가해 해당 조건이 참인 경우에만 코드 블록을 실행하거나 건너뜀
- if/elif/else

---

## 반복문 (loop statement)
- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
    - 특정 작업을 반복적으로 수행
    - 주어진 조건이 참인 동안 반복해서 실행
- for/while

### for statement
- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
    - 임의의 시퀀스, 즉 길이가 있는(개수가 한정적인) 자료형이기 때문에 종료조건을 만들어줄 필요가 없음
    - 반복 가능한 객체(iterable)
        - 반복문에서 순회할 수 있는 객체
        - 시퀀스, dict, set 등. 문자열도!
- 중첩 반복문
    - 안쪽 반복문은 바깥 반복문의 각 항목에 대해 한 번씩 실행됨
    - print가 호출되는 횟수 : len(outers) * len(inners)
    - 중첩 리스트 순회 : 바깥 리스트를 순회하면서 중첩 반복문을 사용해 각 안쪽 반복을 순회

### while statement
- 주어진 조건식이 참인 동안 코드를 반복해서 실행
- 조건식이 거짓이 될 때까지 반복
- while문을 사용한 특정 입력 값에 대한 종료 조건 활용하기
- while문은 반드시 종료조건이 필요

### 적절한 반복문 활용하기
- for
    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 리스트, 튜플, 문자열 등의 시퀀스 형식의 데이터를 처리할 때

- while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### 반복 제어
- for문과 while은 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음
- break
    - 반복을 즉시 중지
- continue
    - 다음 반복으로 건너뜀

---

## List Comprehension
- 간결하고 효율적인 리스트 생성 방법
> `[expression for 변수 in iterable]`
> `list(expression for 변수 in iterable)`

- List Comprehension과 if 조건문 (Comprehension을 남용하지 말자)
> `[expression for 변수 in iterable]`
> `list(expression for 변수 in iterable)`

- loop vs map vs list comprehension
    - 성능은 일반화가 불가능 (외부요인, 상황)
    - 대부분의 상황에서는 list comprehension이 빠르다
    - 하지만 다른 함수, 내장함수에 따라 map이 더 빠른 경우도 많음
    - 파이썬이 3.후반에 for loop 성능에 비약적인 향상이 있었음
    - 그래서 극단적인 차이는 존재하지 않음
    - 코드의 가독성 > 간결함
    - 프로그래밍은 우리 프로그램이 어떻게 그 목적을 명확하게 전달하는지에 대한 것
    - "작은 효율성에 대해서는 말하자면 97% 정도에 대해서는 잊어버려라. 섣부른 최적화는 모든 악의 근원이다"

---

## 참고
- pass
    - 아무런 동작도 수행하지 않고 넘어가는 역할
    - 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용
- enumerate(iterable, start=0)
    - iterable 객체의 각 요소에 대해 인덱스와 함께 반환되는 내장함수
    > `fruits = ['apple', 'banana', 'cherry']`
    > `for index, fruit in enumerate(fruits):`
    > ` print(f"인덱스 {index}: {fruit}")`