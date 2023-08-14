# Get factorial
def factorial(n: int) -> int:
    if n == 1:
        return 1 # Base case
    return n * factorial(n-1) # Recursive case

print(factorial(4))