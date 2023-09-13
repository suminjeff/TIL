## Django Template system
- 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
- DTL (Django Template Language)
  - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
  - 변수 (Variables)
    - 중괄호 2개를 열고 닫기
    - render 함수의 3번쨰 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot(.)을 사용해 변수 속성에 접근할 수 있음
  - 필터
    - 표시할 변수를 수정할 때 사용
    - chained가 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
  - 태그
    - 반복 또는 논리를 수행해 제어 흐름을 만듬
    - 일부 태그는 시작과 종료 태그가 필요 (if-endif, for-endfor)
    - 약 24개의 built-in template tags 제공
  - 주석
- 템플릿 상속
  - 만약 모든 템플릿에 bootstrap을 적용하려면?
  - 기본 skeleton 템플릿을 작성해 상속 구조를 구축
  - extends tag
    - 자식 템플릿에 부모 템플릿을 확장한다는 것을 알림
      - 반드시 템플릿 최상단에 작성되어야 함 (2개 이상 사용 불가)
  - block tag
    - 하위 템플릿에서 재정의할 수 있는 블록을 정의
      - 하위 템플릿이 작성할 수 있는 공간을 지정


## HTML form (요청과 응답)
- form
  - action, method (from의 핵심 속성 2가지)
    - 어디로 어떤 방식으로 요청할지

- input
  - name (input의 핵심 속성)
    - 서버로 보내는 키

- query string parameters


## Django URL
- URL dispatcher
- Variable Routing