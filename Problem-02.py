def even_fibonacci_sum(limit):
    a, b = 1, 2  # First two terms of Fibonacci sequence
    total = 0
    
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b  # Generate next Fibonacci number
    
    return total

# Set the limit to 4 million
limit = 4000000
result = even_fibonacci_sum(limit)
print("Sum of even Fibonacci numbers below 4 million:", result)
