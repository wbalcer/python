def unique_permutations(elements: list):
    def backtrack(path, remaining, result):
        if not remaining:
            result.add(tuple(path))
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:], result)
    
    result = set()
    backtrack([], elements, result)
    return list(result)

elements = [1, 2, 2]
print(unique_permutations(elements))
