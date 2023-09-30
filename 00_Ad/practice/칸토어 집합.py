import sys
sys.stdin = open("칸토어 집합.txt", "r")
input = sys.stdin.readlines

space = " "
line = "-"

def cantor(n):
    if n == 0:
        return line




file = input()
for i in range(len(file)):
    file[i] = int(file[i].rstrip('\n'))

for n in file:
    print(cantor(n))
