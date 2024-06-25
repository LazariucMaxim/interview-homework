import pytest
from main import balanced_brackets


@pytest.mark.parametrize(
    'sequence,expected',
    (
            ['(((([{}]))))', 'Сбалансированно'],
            ['[([])((([[[]]])))]{()}', 'Сбалансированно'],
            ['{{[()]}}', 'Сбалансированно'],
            ['}{}', 'Несбалансированно'],
            ['{{[(])]}}', 'Несбалансированно'],
            ['[[{())}]', 'Несбалансированно']
    )
)
def test_balanced_brackets(sequence, expected):
    actual = balanced_brackets(sequence)
    assert actual == expected
