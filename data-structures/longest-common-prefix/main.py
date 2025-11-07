class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            current_keys = list(current.keys())
            if self.end_symbol in current_keys:
                break
            elif len(current_keys) == 1:
                letter = current_keys[0]
                prefix += letter
                current = current[letter]
            elif len(current_keys) != 1:
                break
        return prefix


    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
