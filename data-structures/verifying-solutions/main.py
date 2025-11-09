def get_num_guesses(length):
    guesses = (26 ** (length + 1) - 26) // 25
    return guesses