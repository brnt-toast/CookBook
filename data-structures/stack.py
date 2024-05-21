class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushes:", stack)
print("Top element (peek):", stack.peek())
print("Pop element:", stack.pop())
print("Stack after pop:", stack)
print("Is stack empty?:", stack.is_empty())
