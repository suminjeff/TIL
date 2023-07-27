class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"안녕. {self.name}"


class Mom(Person):
    gene = 'XX'

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return "엄마가 수영"


class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return "아빠가 걷기"
    

class FirstChild(Dad, Mom):
    dad_gene = Dad.gene
    
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return "첫째가 수영"

    def cry(self):
        return "첫째가 응애"
    
    

baby1 = FirstChild("아가")
print(baby1.cry())
print(baby1.swim())
# print(baby1.walk())
# print(baby1.gene)
print(baby1.dad_gene)

print('---------------')

print(FirstChild.mro())
