def reverse_number(n):
    reversed_num = 0
    
    while n > 0:
        remainder = n % 10
        reversed_num = reversed_num * 10 + remainder
        n = n // 10
    
    return reversed_num

num = int(input("enter a number:"))
reversed_num = reverse_number(num)
print(f"The reversed number is: {reversed_num}")
