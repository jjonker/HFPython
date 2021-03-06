def search_for_vowels(word:str) -> set:
    """Return any vowels found in a given word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
