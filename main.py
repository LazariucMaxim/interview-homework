from models.stack import Stack


def balanced_brackets(sequence: str) -> str:
    stack = Stack()
    for element in sequence:
        if (stack.peek(), element) in (
                ('(', ')'),
                ('[', ']'),
                ('{', '}')
        ):
            stack.pop()
        else:
            stack.push(element)
    return 'Сбалансированно' if stack.is_empty() else 'Несбалансированно'


if __name__ == '__main__':
    print(balanced_brackets(input()))
