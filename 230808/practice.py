def strlen(a):
    count = 0
    while a[0] != '\0':
        a.pop(0)
        count += 1
    return count


a = ['a', 'b', 'c', '\0']
print(strlen(a))