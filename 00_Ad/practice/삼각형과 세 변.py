import sys
sys.stdin = open("삼각형과 세 변.txt", "r")

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    else:
        L = max(a, b, c)
        if L - (a + b + c - L) >= 0:
            print("Invalid")
        else:
            my_set = set()
            my_set.add(a)
            my_set.add(b)
            my_set.add(c)
            if len(my_set) == 3:
                print("Scalene")
            elif len(my_set) == 2:
                print("Isosceles")
            else:
                print("Equilateral")