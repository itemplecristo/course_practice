"""
Module 01: Python Basics & Core Syntax - Practice Tasks
"""


def fizz_buzz(n: int) -> list[str]:
    """
    Return a list of strings from 1 to n where:
    - multiples of 3 are 'Fizz'
    - multiples of 5 are 'Buzz'
    - multiples of both 3 and 5 are 'FizzBuzz'
    - otherwise the number as a string
    """
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    print("Testing FizzBuzz(15):")
    print(fizz_buzz(15))
    print("\nTesting Primes up to 20:")
    primes = [x for x in range(20) if is_prime(x)]
    print(f"Primes: {primes}")
