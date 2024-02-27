my_list = [11, 3, 23, 7]

my_list.append(17)
my_list.pop()

# These are o(1) if we add something or remove something at the end of the list

my_list.pop(0)
my_list.insert(0, 11)

# These would be o(n) because if we would have to reindex
# all the items that were removed or added
# n would be the num of items in list

my_list.insert(1, "Hi")
# This would be o(n) because we would again have to reindex


# If we were to iterate through the list until we got to 7
# it would be o(n), but if we chose a specific index then it would be o(1)
