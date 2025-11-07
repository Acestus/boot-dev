class Trie:
    def advanced_find_matches(self, document, variations):
        variations_map = {}
        for key, value in variations.items():
            variations_map[key] = value
            variations_map[value] = value
        
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                # Use the variation to navigate the trie, but keep original character
                trie_char = variations_map.get(ch, ch)
                if trie_char not in level:
                    break
                level = level[trie_char]
                if self.end_symbol in level:
                    # Add the original substring from the document
                    matches.add(document[i : j + 1])
        return matches


    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
