class Trie:
    def search_level(self, current_level, current_prefix, words):
        if current_level.get(self.end_symbol):
            words.append(current_prefix)
        for letter, next_level in sorted(current_level.items()):
            if letter != self.end_symbol:
                self.search_level(next_level, current_prefix + letter, words)

    def words_with_prefix(self, prefix):
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        words = []
        self.search_level(current_level, prefix, words)
        return words
        

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
