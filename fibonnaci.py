"""Fibonacci module — Lab 1: Software Construction.

Your task is to implement the fibonacci function below following
PEP 8 coding standards. Read the docstring carefully before you begin.
"""

# TODO: Implement the function below.
# Requirements:
#   - Must follow PEP 8 naming and formatting rules
#   - Must handle edge cases (n = 0, n = 1, negative n)
#   - Must include a complete Google-style docstring
#   - Must pass all tests in test_fibonacci.py


def fibonacci(n):
    """Calculate the nth Fibonacci number.

    The Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, ...
    fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, etc.

    Args:
        n: The position in the Fibonacci sequence (must be >= 0).

    Returns:
        The nth Fibonacci number as an integer.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(6)
        8
    """
    # TODO: Replace this with your implementation
    raise NotImplementedError("fibonacci() is not yet implemented.")
    def fibonacci(n):

if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be greater than or equal to 0")

    if n in (0, 1):
        return n

    previous, current = 0, 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current
