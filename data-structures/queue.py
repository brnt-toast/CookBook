class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")


    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Front of empty queue")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue)
print("Front element:", queue.front())
print("Dequeue element:", queue.dequeue())
print("Queue after dequeue:", queue)
print("Is queue empty?:", queue.is_empty())
