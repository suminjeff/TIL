class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"반갑습니다. {self.name}입니다.")


class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 25, 3.5)

p1.talk()
s1.talk()