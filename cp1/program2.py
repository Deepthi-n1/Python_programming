def print_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

num=int(input("enter a number:"))
print_triangle(num)
