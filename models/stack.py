class Stack:
    def __init__(self):
        self._elements = []

    def push(self, element):
        self._elements.append(element)

    def pop(self):
        return self._elements.pop()

    def peek(self):
        return self._elements[-1]

    def size(self):
        return len(self._elements)

    def is_empty(self):
        return not self.size()

    def __str__(self):
        return f'stack({", ".join(map(str, self._elements))})'
