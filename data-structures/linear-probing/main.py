class HashMap:
    def insert(self, key, value):
        i = self.key_to_index(key)
        original_i = i
        
        while self.hashmap[i] is not None and self.hashmap[i][0] != key:
            i = (i + 1) % len(self.hashmap)
            if i == original_i:
                raise Exception("hashmap is full")
        
        self.hashmap[i] = (key, value)              

    def get(self, key):
        i = self.key_to_index(key)
        original_i = i
        
        while self.hashmap[i] is not None:
            if self.hashmap[i][0] == key:
                return self.hashmap[i][1]
            i = (i + 1) % len(self.hashmap)
            if i == original_i:
                raise Exception("sorry, key not found")
        
        raise Exception("sorry, key not found")

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
