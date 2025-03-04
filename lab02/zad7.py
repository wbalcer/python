from collections import Counter

def most_frequent_element(data: list):
    if not data:
        return None
    
    counter = Counter(data)
    most_common = counter.most_common(1)
    return most_common[0][0]

example_list = [1, 3, 2, 3, 4, 3, 2, 2, 2]
print(most_frequent_element(example_list))
