def factorial(n):
    if n < 0:
        raise ValueError("Silnia jest zdefiniowana tylko dla liczb nieujemnych")
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

print(factorial(5))  # 5! = 120
