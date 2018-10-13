import pytest

from chapter_6.exercises import (
    remove_all_elements_from_stack,
    transfer_from_stack_to_stack,
    reverse,
    ArithmeticGroupingSymbolValidator,
    MyQueue
)


class TestTransferFromStackToStackFunction:
    @pytest.mark.parametrize(
        'stack_a, stack_b, expected_result', [
            ([], [], []),
            [[1], [], [1]],
            [[1, 2], [], [2, 1]],
            [[1, 2, 3], [], [3, 2, 1]],
            [[3, 2, 1], ['A', 'B'], ['A', 'B', 1, 2, 3]],
        ]
    )
    def test_transfer_from_stack_to_stack(self, stack_a, stack_b, expected_result):
        transfer_from_stack_to_stack(stack_a=stack_a, stack_b=stack_b)
        assert stack_b == expected_result


class TestRemoveAllElementsFromStackFunction:
    @pytest.mark.parametrize(
        'stack, expected_result', [
            ([], []),
            [[1], []],
            [[1, 2], []],
            [[1, 2, 3], []],
            [[-2, -1, 0, 1, 2, 3], []],
        ]
    )
    def test_remove_all_elements_from_stack(self, stack, expected_result):
        actual_result = remove_all_elements_from_stack(stack=stack)
        assert actual_result == expected_result


class TestReverseFunction:
    @pytest.mark.parametrize(
        'elements, expected_result', [
            ([], []),
            [[1], [1]],
            [[1, 2], [2, 1]],
            [[1, 2, 3], [3, 2, 1]],
            [[-2, -1, 0, 1, 2, 3], [3, 2, 1, 0, -1, -2]],
        ]
    )
    def test_reverse(self, elements, expected_result):
        actual_result = reverse(elements=elements)
        assert actual_result == expected_result

# region TestArithmeticGroupingSymbolValidator
# region test___init__
EXPECTED_PASSING_EMPTY_SYMBOLS = {
    '_left_grouping_symbols': [],
    '_right_grouping_symbols': [],
    '_equivalent': dict()
}
TEST_PASSING_EMPTY_SYMBOLS = (
    [],
    [],
    EXPECTED_PASSING_EMPTY_SYMBOLS
)

TEST_PASSING_PARAMETERS_WITH_ONE_PARENTHESIS = (
    ['('],
    [')'],
    {
        '_left_grouping_symbols': ['('],
        '_right_grouping_symbols': [')'],
        '_equivalent': {')': '('}
    }
)

TEST_PASSING_PARAMETERS_WITH_TWO_PARENTHESIS = (
    ['(', '['],
    [')', ']'],
    {
        '_left_grouping_symbols': ['(', '['],
        '_right_grouping_symbols': [')', ']'],
        '_equivalent': {')': '(', ']': '['}
    }
)
# region test___init__negative
TEST_PASSING_DIFFERENT_SIZE_OF_SYMBOLS = (
    ['('],
    ['(', '[']
)

TEST_PASSING_THE_SAME_SYMBOLS_TWICE = (
    ['(', '('],
    ['(', '[']
)
# endregion test___init__negative
# endregion TestArithmeticGroupingSymbolValidator


class TestArithmeticGroupingSymbolValidator:
    @pytest.mark.parametrize(
        'left_grouping_symbols, right_grouping_symbols, expected_result', [
            TEST_PASSING_EMPTY_SYMBOLS,
            TEST_PASSING_PARAMETERS_WITH_ONE_PARENTHESIS,
            TEST_PASSING_PARAMETERS_WITH_TWO_PARENTHESIS
        ]
    )
    def test___init__(self, left_grouping_symbols, right_grouping_symbols, expected_result):
        assert vars(
            ArithmeticGroupingSymbolValidator(
                left_grouping_symbols=left_grouping_symbols,
                right_grouping_symbols=right_grouping_symbols
            )
        ) == expected_result

    @pytest.mark.parametrize(
        'left_grouping_symbols, right_grouping_symbols', [
            TEST_PASSING_DIFFERENT_SIZE_OF_SYMBOLS,
            TEST_PASSING_THE_SAME_SYMBOLS_TWICE
        ]
    )
    def test___init__negative(self, left_grouping_symbols, right_grouping_symbols):
        with pytest.raises(AssertionError):
            ArithmeticGroupingSymbolValidator(
                left_grouping_symbols=left_grouping_symbols,
                right_grouping_symbols=right_grouping_symbols
            )

    @pytest.mark.parametrize(
        'left_grouping_symbols, right_grouping_symbols,arithmetic_expression, expected_result', [
            (['(', '['], [')', ']'],  '', False),
            (['(', '['], [')', ']'], '1', True),
            (['(', '['], [')', ']'], '(', False),
            (['(', '['], [')', ']'], ')', False),
            (['(', '['], [')', ']'], '()', True),
            (['(', '['], [')', ']'], '()[]', True),
            (['(', '['], [')', ']'], '[()]', True),
            (['(', '['], [')', ']'], '[[]]', True),
            (['(', '['], [')', ']'], '((()))', True),
            (['(', '['], [')', ']'], '(1)', True),
            (['(', '['], [')', ']'], '(-1)', True),
            (['(', '['], [')', ']'], '-(1)', True),
            (['(', '['], [')', ']'], '(1 + 1)', True),
            (['(', '['], [')', ']'], '(1+1)', True),
            (['(', '['], [')', ']'], '((1 + 1)+1)', True),
            (['(', '['], [')', ']'], '(1+1)+(2+2)', True),
            (['(', '['], [')', ']'], '[(1+ 1) / 2]', True),

        ]
    )
    def test_valid_arithmetic_grouping(
            self,
            left_grouping_symbols,
            right_grouping_symbols,
            arithmetic_expression,
            expected_result
    ):
        validator = ArithmeticGroupingSymbolValidator(
            left_grouping_symbols=left_grouping_symbols,
            right_grouping_symbols=right_grouping_symbols
        )
        actual_result = validator.valid_arithmetic_grouping(arithmetic_expression=arithmetic_expression)
        assert actual_result == expected_result


# R-6.11
# Give a simple adapter that implements our queue ADT while using a collections.deque
# instance for storage.
class TestMyQueue:
    def test___init__(self):
        my_queue = MyQueue()
        assert my_queue._queue is not None, '_queue should not be none'

    @pytest.mark.parametrize(
        'elements_to_add, expected_result', [
            ([], list()),
            ([0], [0]),
            ([1, 2], [1, 2]),
            ([2, 1], [2, 1]),
            ([3, 2, 1], [3, 2, 1]),
        ]
    )
    def test_enqueue(self, elements_to_add, expected_result):
        my_queue = MyQueue()
        for element in elements_to_add:
            my_queue.enqueue(element=element)

        assert list(my_queue._queue) == expected_result

    @pytest.mark.parametrize(
        'start_elements, how_many_invokes, expected_result', [
            ([1], 0, [1]),
            ([1], 1, list()),
            ([1, 2], 1, [1]),
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], 2, [1, 2, 3]),
            ([1, 2, 3, 4, 5], 3, [1, 2]),
            ([1, 2, 3, 4, 5], 4, [1]),
            ([1, 2, 3, 4, 5], 5, list()),
        ]
    )
    def test_dequeue(self, start_elements, how_many_invokes, expected_result):
        my_queue = MyQueue(elements=start_elements)
        for _ in range(how_many_invokes):
            my_queue.dequeue()
        assert list(my_queue._queue) == expected_result

    @pytest.mark.parametrize(
        'start_elements, expected_first_element, expected_result', [
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ]
    )
    def test_first(self, start_elements, expected_first_element, expected_result):
        my_queue = MyQueue(elements=start_elements)
        assert list(my_queue._queue) == expected_result
        assert my_queue.first() == expected_first_element

    @pytest.mark.parametrize(
        'start_elements, expected_result', [
            ([1, 2, 3, 4, 5], False),
            ([], True),
        ]
    )
    def test_is_empty(self, start_elements, expected_result):
        my_queue = MyQueue(elements=start_elements)
        assert my_queue.is_empty() == expected_result

