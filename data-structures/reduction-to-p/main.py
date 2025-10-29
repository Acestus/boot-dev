def fib(n):
    # Polynomial-time Fibonacci implementation
    grandparent = 0
    parent = 1
    current = n
    for _ in range(n - 1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    return current

print(fib(0))