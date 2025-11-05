class BSTNode:
    def delete(self, val):
        if not self:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        elif val == self.val:
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            elif self.left and self.right:
                successor_value = self.right.get_min()
                self.val = successor_value
                self.right = self.right.delete(successor_value)
                return self

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.lef
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
