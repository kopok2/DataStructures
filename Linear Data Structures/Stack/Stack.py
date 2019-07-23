class Stack:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
