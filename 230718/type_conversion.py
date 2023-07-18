my_str = 'Hello SSAFY!'
conv_list = list(my_str)
my_list = [my_str]
conv_set = set(my_str)

# print(conv_list)
# print(my_list)
# print(conv_set)


################
##리스트 형변환##
################

my_list = [10, 20, 30, 20, 10]
conv_str = str(my_list)
conv_tup = tuple(my_list)
conv_set = set(my_list)
conv_list = list(my_list)

print(conv_str, type(conv_str))
print(conv_tup, type(conv_tup))
print(conv_set, type(conv_set))
print(conv_list, type(conv_list))