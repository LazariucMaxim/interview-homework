from typing import Any


class Stack:
    _elements: list

    def __init__(self) -> None:
        self._elements = []

    def push(self, element: Any) -> None:
        self._elements.append(element)

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return not self.size()

    def pop(self) -> Any:
        return self._elements.pop()

    def peek(self) -> Any:
        if not self.is_empty():
            return self._elements[-1]

    def __str__(self) -> str:
        return f'stack({", ".join(map(str, self._elements))})'
