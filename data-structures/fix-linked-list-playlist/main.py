class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def push_back(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def pop_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            # Single node case
            value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return value
        
        # Find the second-to-last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # Remove the last node
        value = current.next.value
        current.next = None
        self.tail = current
        self.size -= 1
        return value

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
