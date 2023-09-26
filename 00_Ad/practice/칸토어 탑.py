import sys
sys.stdin = open("칸토어 탑.txt", "r")
input = sys.stdin.readlines

file = input()
for i in range(len(file)):
    file[i] = file[i].rstrip('\n')
print(file)