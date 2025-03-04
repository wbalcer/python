def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text
    
    text_list = list(text)
    for i in range(key - 1, len(text), key):
        if i + key < len(text):
            text_list[i], text_list[i + key] = text_list[i + key], text_list[i]
    
    print(text_list)

transposition_cipher("abcdefghijklm", 3)
