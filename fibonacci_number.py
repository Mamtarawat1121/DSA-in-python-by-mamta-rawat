def fibonacci(num):
    if num==0 or num == 1:
        return num
    return fibonacci(num-1) + (num - 2)
print(fibonacci(7))

# tc = o(2^n)
