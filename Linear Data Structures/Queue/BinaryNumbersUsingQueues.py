"""Generate and print n binary numbers using queues."""

from Queue import Queue


def n_binary(n):
    q = Queue()
    q.enqueue("1")
    for x in range(n):
        c = q.dequeue()
        print(c)
        q.enqueue(c + "0")
        q.enqueue(c + "1")


if __name__ == "__main__":
    n_binary(100)
