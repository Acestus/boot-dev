class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            new_size = 1
            self.hashmap = [None]
            return None
        elif self.current_load() < 0.05:
            return None
        else:
            temp = self.hashmap
            new_size = len(self.hashmap) * 10
            self.hashmap = [None for i in range(new_size)]
            for item in temp:
                if item is not None:
                    index = self.key_to_index(item[0])
                    self.hashmap[index] = item

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        return sum(1 for item in self.hashmap if item is not None) / len(self.hashmap)

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
