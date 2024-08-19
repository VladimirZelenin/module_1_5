immutable_var = tuple([1, 2, 3, False, "flout"])
print(immutable_var)
# immutable_var[0] = 35
# print(immutable_var) - кортеж не поддерживает обращение по элементам!!!
mutable_list = [1, 2, 'y', 'n', 'String']
mutable_list[1] = 77
print(mutable_list)