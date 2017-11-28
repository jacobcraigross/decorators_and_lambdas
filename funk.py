#
# def methodception(another):
#     return another()
#
# def add_two_numbers():
#     return 44 + 88
#
# #lambda function
# print(methodception(lambda: 44 + 88))


#functional programming notes
my_list = [22, 44, 66, 77, 99, 101, 444, 333, 221, 888, 1, 3, 5, 7, 9]

# a basic way to remove an item from the list would be to...
#my_list.remove(44)

# but say you wanted to remove all ODD numbers... use a built in method called filter
print (list(filter(lambda x: x % 2 != 0, my_list)))
