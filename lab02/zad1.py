def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True if n > 1 else False

def prime_selector(numbers: list[int]):
    output = []
    for n in numbers:
        if is_prime(n):
            output.append(n)
    print(output)


numbers = [3,4,5,1,2,10,4,50]
prime_selector(numbers)