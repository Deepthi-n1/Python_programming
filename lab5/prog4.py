row = int(input("Enter the number of rows:"))
for i in range(1, row + 1):
    print(" " * (row - i) + " ".join(str(num) for num in range(1, i + 1)))
