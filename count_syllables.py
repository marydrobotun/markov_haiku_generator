import sys
from string import punctuation
import json

vowels = ["у", "е", "ё", "ы", "а", "о", "э", "я", "и", "ю"]


def count_syllables(words):
    """Сounts syllables in Russian word or phrase."""
    words = words.replace('-', ' ')
    words = words.lower().split()
    num_sylls = 0
    for word in words:
        word = word.strip(punctuation)
        for chr in word:
            if chr in vowels:
                num_sylls += 1
    return num_sylls
