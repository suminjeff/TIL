import sys
sys.stdin = open("칸토어 집합.txt", "r")
input = sys.stdin.readlines

space = " "
line = "-"


def cantor(n):
    if n == 1:
        return line

    left = cantor(n//3)
    middle = space * (n//3)
    right = cantor(n//3)
    cantor_string = left+middle+right
    return cantor_string


file = input()
for i in range(len(file)):
    file[i] = int(file[i].rstrip('\n'))

for n in file:
    print(cantor(3**n))
