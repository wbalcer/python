def czy_anagram(s1: str, s2: str) -> bool:
    s1 = s1.lower()
    s2 = s2.lower()
    
    return sorted(s1) == sorted(s2)

print(czy_anagram("Agr", "Gra"))
