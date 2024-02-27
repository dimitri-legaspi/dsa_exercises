def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)

# This ran n + n times or 2n times but we can simplify
# it to just o(n) by dropping the constant.
