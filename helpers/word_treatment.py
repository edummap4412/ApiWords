import json


def vowel_count(words: dict) -> dict:
    result = {}
    for word in words:
        vowels = [char for char in word if char.lower() in 'aeiou']
        result[word] = len(vowels)

    return result


def sort_words(words, reverse):
    reverso = {'words': words[::-1], 'order': 'desc'} if reverse else {'words': words, 'order': 'asc'}
    return reverso
