class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def get_items(self):
        return self.items

    def peek(self):
        return self.items[0]


class QueuezyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def get_items(self):
        return self.q1.get_items()

    def push(self, value):
        self.q2.enqueue(value)
        while not self.q1.is_empty():
            v = self.q1.dequeue()
            self.q2.enqueue(v)
        swap = self.q1
        self.q1 = self.q2
        self.q2 = swap

    def pop(self):
        return self.q1.dequeue()

    def peek(self):
        return self.q1.peek()

    def is_empty(self):
        return self.q1.is_empty()
