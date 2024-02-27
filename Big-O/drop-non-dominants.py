def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(10)

# this would be o(n)^2 + o(n) which would be o(n^2 + n)
# we would drop the n because the n^2 is more dominant thatn the n therefore
# it becomes O(n^2)
