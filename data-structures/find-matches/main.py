class Trie:
    def find_matches(self, document):
        matches = set()
        doc_length = len(document)
        for i in range(doc_length):
            current = self.root
            j = i
            while j < doc_length:
                letter = document[j]
                if letter not in current:
                    break
                current = current[letter]
                if self.end_symbol in current:
                    matches.add(document[i:j+1])
                j += 1
        return list(matches)
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
