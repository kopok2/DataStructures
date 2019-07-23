"""Queue Python implementation using stacks."""


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


class QueueUsingStacks:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def get_items(self):
        return self.s1.get_items()[::-1]

    def is_empty(self):
        return self.s1.is_empty()

    def enqueue(self, value):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s1.push(value)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

    def front(self):
        return self.s1.peek()

    def rear(self):
        while not self.s1.is_empty():
            v = self.s1.pop()
            last = v
            self.s2.push(v)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        return last
