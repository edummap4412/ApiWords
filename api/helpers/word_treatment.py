

def vowel_count(words: list):
    result = {}
    for word in words:
        vowels = [char for char in word if char.lower() in 'aeiou']
        result[word] = len(vowels)
    return result


def sort_words(words: list, order: str):
    return words[::-1] if order == 'desc' else words


def validate_words(value):
    if not isinstance(value, list) or not all(isinstance(word, str) for word in value):
        raise ValueError("Value is not a valid list of strings")
    return value
