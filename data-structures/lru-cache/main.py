from functools import lru_cache


@lru_cache()
def is_palindrome(word):
    if len(word) < 2:
        return True
    first = word[0]
    last = word[-1]
    if first != last:
        return False
    trimmed_word = word[1:-1]
    return is_palindrome(trimmed_word)
