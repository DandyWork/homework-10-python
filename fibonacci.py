def generate_fibonacci(n):
    """
    Generate a Fibonacci sequence with n terms.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

