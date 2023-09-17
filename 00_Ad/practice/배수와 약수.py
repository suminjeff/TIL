import sys

sys.stdin = open("배수와 약수.txt", "r")

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        if A % B == 0 or B % A == 0:
            if A % B == 0:
                print("multiple")
            else:
                print("factor")
        else:
            print("neither")