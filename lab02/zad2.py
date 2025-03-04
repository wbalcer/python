def round_numbers(numbers: list[int], threshold: int):
    output = []
    for n in numbers:
        if n < threshold:
            n = n - (n % 10)
            output.append(n)
        else:
            n = n - (n % 10) + 10
            output.append(n)
    print(output)

numbers = [12, 32, 45, 60, 44]
round_numbers(numbers, 40)