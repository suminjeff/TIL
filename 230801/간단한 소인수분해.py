import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    elements = [2, 3, 5, 7, 11]
    element_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    for i in elements:
        while N % i == 0:
            N = N // i
            element_dict[i] += 1

    print(f"#{tc}", *element_dict.values())
