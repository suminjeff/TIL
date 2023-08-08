def itoa(a):
    s = ''
    while a > 0:
        s += chr(ord('0') + a % 10)
        a //= 10
    return s

print(itoa(123456789))