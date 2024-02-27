def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# This would be o(a + b), there is no way of simplifying this
# o(a) + o(b) = o(a+ b)


def print_items_again(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

# This would be o(a) * o(b) which would be o(a * b).
