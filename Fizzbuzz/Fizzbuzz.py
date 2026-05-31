def fizzbuzz(n):
    """
    Returns 'Fizzbuzz' if n is divisible by 3 and 5,
    'Fizz' if divisible by 3,
    'Buzz' if divisible by 5,
    and the number n itself otherwise.
    """
    # We must check for BOTH 3 and 5 first!
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    # Then check for 3
    elif n % 3 == 0:
        return "Fizz"
    # Then check for 5
    elif n % 5 == 0:
        return "Buzz"
    # If none of the above are true, just return the number
    else:
        return n

def main():
    # Play Fizz Buzz from 1 up to 17 (inclusive)
    for i in range(1, 18):
        result = fizzbuzz(i)
        print(result)

if __name__ == '__main__':
    main()
