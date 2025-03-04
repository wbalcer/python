def fibonacci_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

gen = fibonacci_generator(10)
print(list(gen))
