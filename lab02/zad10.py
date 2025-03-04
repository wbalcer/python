from collections import defaultdict

def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    grouped_words = defaultdict(list)
    
    for word in words:
        grouped_words[len(word)].append(word)
    
    return dict(grouped_words)

words_list = ["test", "testy", "tes", "tset", "testest", "sety"]
result = group_words_by_length(words_list)
print(result)