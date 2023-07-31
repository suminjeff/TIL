# 비시퀀스 데이터 구조
## 세트
- 고유한 항목들의 정렬되지 않은 컬렉션
- 세트 메서드
    - `s.add(x)` : 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
    - `s.clear()` : 세트 s의 모든 항목을 제거
    - `s.remove(x)` : 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error
    - `s.pop()` : 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
    - `s.discard()` : 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
    - `s.update(iterable)` : 세트 s에 다른 iterable 요소를 추가

- 세트의 집합 메서드
    - `set1.difference(set2)` : set1에 있지만 set2에는 없는 항목으로 세트 생성 후 반환 (set1 - set2)
    - `set1.intersection(set2)` : set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환 (set1 & set2)
    - `set1.issubset(set2)` : set1의 항목이 모두 set2에 들어있으면 True (set1 <= set2>)
    - `set1.issuperset(set2)` : set1이 set2의 항목을 모두 포함하면 True를 반환 (set1 >= set2)
    - `set1.union(set2)` : set1 또는 set2에 (혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환 (set1 | set2)


## 딕셔너리
- 고유한 항목들의 정렬되지 않은 컬렉션
- 딕셔너리 메서드
    - `D.clear` : 딕셔너리 D의 모든 키/값 쌍을 제거
    - `D.get(k)` : 키 k에 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
    - `D.get(k, v)` : 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환
    - `D.keys()` : 딕셔너리 키를 모은 객체를 반환
    - `D.values` : 딕셔너리 값을모든 객체를 반환
    - `D.items` : 딕셔너리 키/값 쌍을 모은 객체를 반환
    - `D.pop(k)` : 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default를 반환)
    - `D.pop(k, v)` : 키를 제거하고 연결됐던 값을 반환 (없으면 v를 반환)
    - `D.setdefault(k, v)` : 키와 연결된 값을 반환. 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
    - `D.update(other)` : other가 제공하는 키/값 쌍으로 딕셔너리를 갱신. 기존 키는 덮어씀 (딕셔너리를 넣어도 되고, 키워드 인자를 넣어도 됨)

# 복사
- 데이터 타입과 복사
    - 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
    - 변경 가능한 데이터 타입과 변경 불가능한 데이터 타입을 다르게 다룸
- 복사 유형
1. 할당
    - 같은 주소를 복사
    - 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
1. 얕은 복사
    - 슬라이싱으로 잘라서 새로운 리스트를 반환 [:]
    - 내장함수 copy : `.copy()`
    - 얕은 복사의 한계 : 중첩 리스트는 독립적인 복사본이 만들어지지 않음
        - `a = [1, 2, [1, 2]]`
        - `b = a[:]`
        - `b[2][0] = 999`
        - `print(a, b)` # [1, 2, [999, 2]] [1, 2, [999, 2]]
        - `c = a.copy()`
        - `c[2][0] = 999`
        - `print(a, c)` # [1, 2, [999, 2]] [1, 2, [999, 2]]

1. 깊은 복사
- `import copy` `copy.deepcopy(x)`
- 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함