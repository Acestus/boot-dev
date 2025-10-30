class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)
