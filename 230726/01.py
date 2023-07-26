# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    # 매직 메서드 (생성자 메서드)
    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다'
    
singer1 = Person('iu')
print(singer1.singing())