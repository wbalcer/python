import re

def count_syllables(word):
    vowels = "aeiouyAEIOUY"
    word = word.lower()
    count = 0
    prev_char_was_vowel = False
    
    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    
    if word.endswith("e") and count > 1:
        count -= 1
    
    return max(count, 1)

def readability_score(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    words = text.split()
    num_words = len(words)
    num_sentences = len(sentences)
    num_syllables = sum(count_syllables(word) for word in words)
    
    if num_sentences == 0 or num_words == 0:
        return 0
    
    avg_words_per_sentence = num_words / num_sentences
    avg_syllables_per_word = num_syllables / num_words
    
    return round(avg_words_per_sentence + avg_syllables_per_word, 2)

text = "Ala ma kota kot ma ale"
print(readability_score(text))
