class Person:
    name = 'unknown'
    @classmethod
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

p2 = Person()
p2.talk()
p2.name = 'Kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)