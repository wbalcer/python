def longest_increasing_subsequence(sequence: list[int]):
    output = 1
    curr = 1

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            curr += 1
            output = max(output, curr)
        else:
            curr = 1

    print(output)

sequence = [3, 4, 6, 2, 3, 7, 9, 10, 11]
longest_increasing_subsequence(sequence)
