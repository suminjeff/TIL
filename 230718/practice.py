# 진법 변경
print(bin(12))
print(oct(12))
print(hex(12))

print(2 / 3)

print (5 / 3)

a = 3.2 - 3.1
b = 1.2 - 1.1

# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10)

# 2. math 모듈 사용
import math
print(math.isclose(a, b))

# 지수 표현
print(314e-2, type(314e-2))

# f-string
bugs = 'roaches'
counts = 13
area = 'room'

print(f"Debugging {bugs} {counts} {area}")
fstring = f"Debugging {bugs} {counts} {area}"
print(fstring[-1])


# f-string 응용
greeting = 'hi'

print(f'{greeting:>10}')
print(f'{3.141592:.4f}')

# 불변과 가변
my_str = 'hello'
# my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)

print(ord('A'))