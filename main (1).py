def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# You can change the value of 'n' to generate different Fibonacci numbers.
n = 10  # Change this to the desired Fibonacci number you want to generate.
if n <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
      