import itertools
from typing import List, Dict

import pytest

from chapter_6.exercises import (
    remove_all_elements_from_stack,
    transfer_from_stack_to_stack,
    reverse,
    ArithmeticGroupingSymbolValidator,
    MyQueue,
    ArrayStackWithMaxLen,
    FullException,
    ArrayStackWithInitialization,
    EmptyException,
    reverse_values_in_stack,
    is_matched_html,
    get_tag_name,
    permute_with_stack,
    get_all_subsets,
    ArithmeticExpressionToPostfixExpression,
    move_elements_stack_t_to_stack_s_with_original_sequence,
    SimpleQueueWithTwoStacks,
    has_element_in_stack,
    ArrayDeque,
    LeakyStack,
    PostfixNotationCalculator,
)
from utils.errors import EmptyCollection


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


class TestArrayStack:
    # C - 6.16 Modify the ArrayStack implementation so that the stack’s capacity is limited
    # to maxlen elements, where maxlen is an optional parameter to the constructor
    # (that defaults to None). If push is called when the stack is at full capacity,
    # throw a Full exception (defined similarly to Empty).
    @pytest.mark.parametrize(
        'maxlen, expected_result', [
            (1, {'_data': [], '_maxlen': 1}),
            (None, {'_data': [], '_maxlen': None})
        ]
    )
    def test___init__(self, maxlen, expected_result):
        actual_result = ArrayStackWithMaxLen(maxlen=maxlen)
        assert vars(actual_result) == expected_result

    @pytest.mark.parametrize(
        'array_stack, element, expected_result', [
            (ArrayStackWithMaxLen(maxlen=None), 1, {'_data': [1], '_maxlen': None}),
            (ArrayStackWithMaxLen(maxlen=1), 1, {'_data': [1], '_maxlen': 1}),
        ]
    )
    def test_push(self, array_stack: ArrayStackWithMaxLen, element, expected_result):
        array_stack.push(e=element)
        assert vars(array_stack) == expected_result

    # C - 6.16 Modify the ArrayStack implementation so that the stack’s capacity is limited
    # to maxlen elements, where maxlen is an optional parameter to the constructor
    # (that defaults to None). If push is called when the stack is at full capacity,
    # throw a Full exception (defined similarly to Empty).
    @pytest.mark.parametrize(
        'array_stack, element', [
            (ArrayStackWithMaxLen(maxlen=0), 1),
        ]
    )
    def test_push_exceeded_maxlen(self, array_stack: ArrayStackWithMaxLen, element):
        with pytest.raises(FullException):
            array_stack.push(e=element)


# C-6.17 n the previous exercise, we assume that the underlying list is initially empty.
# Redo that exercise,
# this time preallocating an underlying list with length equal to the stack’s maximum capacity.
class TestArrayStackWithInitialization:
    @pytest.mark.parametrize(
        'maxlen, expected_result', [
            (1, {'_data': [None], '_top_of_stack_index': 0}),
            (2, {'_data': [None, None], '_top_of_stack_index': 0}),

        ]
    )
    def test___init__(self, maxlen, expected_result):
        actual_result = ArrayStackWithInitialization(maxlen=maxlen)
        assert vars(actual_result) == expected_result

    @pytest.mark.parametrize(
        'array_stack, elements_to_add, expected_result', [
            (
                ArrayStackWithInitialization(maxlen=3),
                [1],
                {
                    '_data': [1, None, None],
                    '_top_of_stack_index': 1
                }
            ),
            (
                ArrayStackWithInitialization(maxlen=3),
                [1, 2],
                {
                    '_data': [1, 2, None],
                    '_top_of_stack_index': 2
                }
            ),
            (
                ArrayStackWithInitialization(maxlen=3),
                [1, 2, 3],
                {
                    '_data': [1, 2, 3],
                    '_top_of_stack_index': 3
                }
            ),
        ]
    )
    def test_push(self, array_stack: ArrayStackWithInitialization, elements_to_add, expected_result):
        add_elements_to_stack(array_stack, elements_to_add)
        actual_result = vars(array_stack)
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'array_stack, elements_to_add', [
            (
                ArrayStackWithInitialization(maxlen=3),
                [1, 2, 3, 4]
            ),
        ]
    )
    def test_push__stack_if_full(
            self,
            array_stack: ArrayStackWithInitialization,
            elements_to_add,
    ):
        with pytest.raises(FullException):
            add_elements_to_stack(array_stack, elements_to_add)

    @pytest.mark.parametrize(
        'array_stack, elements_to_add, expected_result', [
            (
                ArrayStackWithInitialization(maxlen=5),
                [],
                True
            ),
            (
                ArrayStackWithInitialization(maxlen=5),
                [1],
                False
            )
        ]
    )
    def test_is_empty(
            self,
            array_stack: ArrayStackWithInitialization,
            elements_to_add, expected_result
    ):
        add_elements_to_stack(array_stack, elements_to_add)

        actual_result = array_stack.is_empty()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'array_stack, elements_to_add, expected_result', [
            (
                    ArrayStackWithInitialization(maxlen=5),
                    [1],
                    1
            ),
            (
                    ArrayStackWithInitialization(maxlen=5),
                    [1, 2],
                    2
            )
        ]
    )
    def test_top(self, array_stack, elements_to_add, expected_result):
        add_elements_to_stack(array_stack, elements_to_add)
        actual_result = array_stack.top()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'array_stack, elements_to_add', [
            (
                    ArrayStackWithInitialization(maxlen=5),
                    [],
            )
        ]
    )
    def test_top_empty_stack(self, array_stack, elements_to_add):
        with pytest.raises(EmptyException):
            add_elements_to_stack(array_stack, elements_to_add)

            array_stack.top()

    @pytest.mark.parametrize(
        'array_stack, elements_to_add, expected_stack_state, expected_popped_value', [
            (
                ArrayStackWithInitialization(maxlen=3),
                [1, 2, 3],
                {
                    '_data': [1, 2, None],
                    '_top_of_stack_index': 2,
                },
                3
            ),
            (
                ArrayStackWithInitialization(maxlen=3),
                [1, 2],
                {
                    '_data': [1, None, None],
                    '_top_of_stack_index': 1
                },
                2
            ),
            (
                ArrayStackWithInitialization(maxlen=3),
                [1],
                {
                    '_data': [None, None, None],
                    '_top_of_stack_index': 0
                },
                1
            ),
        ]
    )
    def test_pop(self, array_stack, elements_to_add, expected_stack_state, expected_popped_value):
        add_elements_to_stack(array_stack, elements_to_add)
        actual_popped_value = array_stack.pop()
        actual_stack_state = vars(array_stack)
        assert actual_stack_state == expected_stack_state
        assert actual_popped_value == expected_popped_value

    @pytest.mark.parametrize(
        'array_stack, elements_to_add', [
            (
                    ArrayStackWithInitialization(maxlen=5),
                    [],
            )
        ]
    )
    def test_pop_empty_stack(self, array_stack, elements_to_add):
        with pytest.raises(EmptyException):
            add_elements_to_stack(array_stack, elements_to_add)

            array_stack.pop()


def add_elements_to_stack(array_stack, elements_to_add):
    for element_to_add in elements_to_add:
        array_stack.push(e=element_to_add)


class TestReverseValuesInStackFunction:
    @pytest.mark.parametrize(
        'stack, expected_value', [
            ([], []),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([1, 2, 3], [3, 2, 1]),
        ]
    )
    def test(self, stack, expected_value):
        actual_result = reverse_values_in_stack(stack=stack)
        assert actual_result == expected_value


class TestIsMatchedHtmlFunction:
    @pytest.mark.parametrize(
        'raw_html, expected_value', [
            ('<>', False),
            ('<a>', False),
            ('<a>a</a>', True),
            ('<a></a>', True),
            ('<body><a></a></body>', True),
            ('<body>eee<a>df</a></body>', True),
            ('body', True),
            ('<a border="3"></a>', True),
            ('<a border="3" with="45"></a>', True),
            ('<a border="3" with="45"    ></a>', True),
            ('<a border="3"    with="45"></a>', True),
            ('<a    border="3" with="45"></a>', True),
            ('<a border="3" with="45"></a>      ', True),
            ('<a border="3" with="45"><text text="bold"></text></a>      ', True),


        ]
    )
    def test_is_matched_html(self, raw_html: str, expected_value):
        actual_result = is_matched_html(raw=raw_html)
        assert actual_result == expected_value

    @pytest.mark.parametrize(
        'raw_tag, expected_result', [
            ('body', 'body'),
            (' body', 'body'),
            ('body border="3"', 'body'),
            ('body border="3" ', 'body'),
            ('body border="3" with="45"    ', 'body'),
            ('body border="3"    with="45"', 'body'),
            ('body    border="3" with="45"', 'body'),
            (' a href="https://onet.pl', 'a')
                ]
    )
    def test__get_tag_name(self, raw_tag: str, expected_result):
        tag = get_tag_name(raw_tag=raw_tag)
        assert tag == expected_result


# class TestCalculateNonRecursiveCombinationsFunction:
#     @pytest.mark.parametrize(
#         'numbers, is_unique_permutations, expected_result', [
#             (list(), False, list()),
#             ([1], False, [[1]]),
#             ([1, 2], False, [[1, 2], [2, 1], [1], [2]]),
#
#         ]
#     )
#     def calculate_non_recursive_combinations(self, numbers, is_unique_permutations, expected_result):
#         actual_result = calculate_non_recursive_combinations(
#             numbers=numbers,Ń
#             is_unique_permutations=is_unique_permutations
#         )
#         assert sorted(actual_result) == sorted(expected_result)

class TestPermuteWithStackFunction:
    @pytest.mark.parametrize(
            'numbers, expected_result', [
                (list(), itertools.permutations(list())),
                ([1], itertools.permutations([1])),
                ([1, 2], list(itertools.permutations([1, 2]))),
                ([1, 2, 3], itertools.permutations([1, 2, 3])),
                ([1, 2, 3, 4], itertools.permutations([1, 2, 3, 4])),
            ]
        )
    def test_permute_with_stack(self, numbers, expected_result):
        actual_result = permute_with_stack(numbers=numbers)
        assert sorted(actual_result) == sorted(expected_result)


class TestGetAllSubsets:
    @pytest.mark.parametrize(
        'numbers, expected_result', [
            ([], [[]]),
            ([1], [[], [1]]),
            ([1, 2], [[], [1], [2], [1, 2]]),
            ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        ]
    )
    def test_get_all_subsets(self, numbers, expected_result):
        actual_result = get_all_subsets(numbers)
        assert sorted(actual_result) == sorted(expected_result)


class TestArithmeticExpressionToPostfixExpression:
    @pytest.mark.parametrize(
        'expression, expected_result', [
            ('', list()),
            ('1 + 1', [1.0, 1.0, '+']),
            ('1 + 1 - 2', [1.0, 1.0, 2.0, '-', '+']),
            ('1 + 1 * 3', [1.0, 1.0, 3.0, '*', '+']),
            ('1 * 4 + 3', [1.0, 4.0, '*', 3.0, '+']),
            ('1 + 2 * 5 + 1 + 2', [1.0, 2.0, 5.0, '*', '+', 1.0, 2.0, '+', '+']),
            ('1 + 2 * 5 + 10 / 2', [1.0, 2.0, 5.0, '*', '+', 10.0, 2.0, '/', '+']),
            ('( )', list()),
            (' ( ( ( ( ) ) ) )', list()),
            ('( 1 + 1 )', [1.0, 1.0, '+']),
            ('1 + 2 + ( 2 * 6 ) + 5', [1.0, 2.0, 2.0, 6.0, '*', 5.0, '+', '+', '+']),
            ('( ( 5 + 2 ) * ( 8 - 3 ) ) / 4', [5.0, 2.0, '+', 8.0, 3.0, '-', '*', 4.0, '/'])

        ]
    )
    def test_parse(self, expression: str, expected_result: List[str]):
        parser = ArithmeticExpressionToPostfixExpression()
        actual_result = parser.parse(expression_elements=expression)
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'operators, expected_result', [
            ([], None),
            (['+'], '+'),
            (['-', '+'], '+'),
            (['-', '('], None),
            (['-', '(', '('], None),
            (['(', '-'], '-'),
        ]
    )
    def test__find_last_arithmetic_operator(self, operators, expected_result):
        actual_result = (
            ArithmeticExpressionToPostfixExpression()._find_last_arithmetic_operator_before_first_open_parenthesis(
                operators=operators,
            )
        )
        assert actual_result == expected_result


class TestMoveElementsStackTToStackSWithOriginalSequence:
    @pytest.mark.parametrize(
        'r, s, t, expected_r, expected_s, expected_t', [
            ([1, 2, 3], [4, 5], [6, 7, 8, 9], [1, 2, 3], [6, 7, 8, 9, 4, 5], [])
        ]
    )
    def test_move_elements_stack_t_to_stack_s_with_original_sequence(
            self,
            r,
            s,
            t,
            expected_r,
            expected_s,
            expected_t,
    ):
        new_r, new_s, new_t = move_elements_stack_t_to_stack_s_with_original_sequence(
            r=r,
            s=s,
            t=t,
        )
        assert new_r == expected_r
        assert new_s == expected_s
        assert new_t == expected_t


class TestSimpleQueueWithTwoStacks:
    @pytest.mark.parametrize(
        'elements_to_add, expected_result', [
            ([1], {'_stack_for_adding_elements': [1], '_stack_for_removing_elements': list()}),
            ([1, 2], {'_stack_for_adding_elements': [1, 2], '_stack_for_removing_elements': list()}),
            ([1, 2, 3], {'_stack_for_adding_elements': [1, 2, 3], '_stack_for_removing_elements': list()})
        ]
    )
    def test_enqueue(self, elements_to_add: List[object], expected_result: Dict[str, object]):
        queue = SimpleQueueWithTwoStacks()
        for element in elements_to_add:
            queue.enqueue(element)

        assert vars(queue) == expected_result

    @pytest.mark.parametrize(
        'stack_for_adding_elements, stack_for_removing_elements, expected_result', [
            (list(), list(), True),
            ([1], list(), False),
            (list(), [1], False),
        ]
    )
    def test_is_empty(
            self,
            stack_for_adding_elements: List[object],
            stack_for_removing_elements: List[object],
            expected_result: bool,
    ):
        queue = SimpleQueueWithTwoStacks(
            stack_for_adding_elements=stack_for_adding_elements,
            stack_for_removing_elements=stack_for_removing_elements,
        )
        assert queue.is_empty() == expected_result

    @pytest.mark.parametrize(
        'elements_to_add, expected_result', [
            ([1], 1),
            ([1, 2], 2),
            ([1, 2, 3], 3),
        ]
    )
    def test_first(self, elements_to_add: List[object], expected_result: object):
        queue = SimpleQueueWithTwoStacks()
        self._add_element_to_queue(queue=queue, elements=elements_to_add)

        assert queue.first() == expected_result

    @staticmethod
    def _add_element_to_queue(queue: SimpleQueueWithTwoStacks, elements: List[object]):
        for element in elements:
            queue.enqueue(element)

    def test_first_negative_scenario_with_no_elements_in_queue(self):
        queue = SimpleQueueWithTwoStacks()
        with pytest.raises(ValueError):
            queue.first()

    @pytest.mark.parametrize(
        'stack_for_adding_elements, stack_for_removing_elements, expected_result', [
            (list(), list(), 0),
            ([1], list(), 1),
            (list(), [1], 1),
            ([1], [1], 2),
            ([1, 2], [1, 2], 4),
        ]
    )
    def test___len__(
            self,
            stack_for_adding_elements: List[object],
            stack_for_removing_elements: List[object],
            expected_result: int,
    ):
        queue = SimpleQueueWithTwoStacks(
            stack_for_adding_elements=stack_for_adding_elements,
            stack_for_removing_elements=stack_for_removing_elements,
        )
        assert len(queue) == expected_result

    @pytest.mark.parametrize(
        'stack_for_adding_elements, stack_for_removing_elements, expected_result', [
            ([1], list(), 1),
            (list(), [1], 1),
            ([1], [2], 2),
            ([1, 2], [3, 4], 4),
            ([4, 3], [], 4)
        ]
    )
    def test_dequeue(
            self,
            stack_for_adding_elements: List[object],
            stack_for_removing_elements: List[object],
            expected_result: bool,
    ):
        queue = SimpleQueueWithTwoStacks(
            stack_for_adding_elements=stack_for_adding_elements,
            stack_for_removing_elements=stack_for_removing_elements,
        )
        assert queue.dequeue() == expected_result

    def test_dequeue_negative_scenario_with_no_elements_in_queue(self):
        queue = SimpleQueueWithTwoStacks()
        with pytest.raises(ValueError):
            queue.dequeue()


class TestIsContainElementInStackFunction:
    @pytest.mark.parametrize(
        'stack, element_to_find, expected_result', [
            ([], 1, False),
            ([2], 1, False),
            ([2, 3, 4, 5], 1, False),
            ([2, 3, 4, 1], 1, True),
            ([2, 3, 1, 3], 1, True),
            ([1, 3, 6, 3], 1, True),
            ([1, 3, 1, 3], 1, True),
        ]
    )
    def test_has_element_in_stack(self, stack, element_to_find,  expected_result):
        stack_copy = list(stack)
        actaul_result = has_element_in_stack(
            stack=stack,
            element_to_find=element_to_find
        )
        assert stack == stack_copy, 'Elements should be in the same order'
        assert actaul_result == expected_result


class TestArrayDeque:
    @pytest.mark.parametrize(
        'initial_length, array, expected_result', [
            (1, None, {'_index_after_last_element': 0, '_size': 0, '_array': [None]}),
        ]
    )
    def test___init__passed_array_is_none(self, initial_length, array, expected_result):
        array_deque = ArrayDeque(initial_length=initial_length, array=array)
        actual_result = array_deque.to_dict()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'array, expected_result', [
            (
                    [None, None, None, None],
                    {'_index_after_last_element': 0, '_size': 0, '_array': [None, None, None, None]}
            ),
        ]
    )
    def test___init__passed_4_element_array(self, array, expected_result):
        array_deque = ArrayDeque(array=array)
        actual_result = array_deque.to_dict()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'array, expected_result', [
            (list(), {'_index_after_last_element': 0, '_size': 0, '_array': [None] * 16}),
        ]
    )
    def test___init__passed_empty_array(self, array, expected_result):
        array_deque = ArrayDeque(array=array)
        actual_result = array_deque.to_dict()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'expected_result', [
            ({'_index_after_last_element': 0, '_size': 0, '_array': [None]*16})
        ]
    )
    def test___init__with_default_values(self, expected_result):
        array_deque = ArrayDeque()
        actual_result = array_deque.to_dict()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, expected_result', [
            (15, 15),
            (14, 14),
        ]
    )
    def test__get_index_after_last_element(self, index_after_last_element, expected_result):
        array_queue = ArrayDeque()
        array_queue._index_after_last_element = index_after_last_element
        actual_result = array_queue._get_index_after_last_element()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, initial_length, expected_result', [
            (0, 0, 4, 0),
            (0, 1, 4, 2),
            (1, 2, 4, 2),
            (1, 3, 4, 1),
            (1, 4, 4, 0),
        ]
    )
    def test__get_index_before_first_element(self, index_after_last_element, size, initial_length,  expected_result):
        array_queue = ArrayDeque(initial_length=initial_length)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        actual_result = array_queue._get_index_before_first_element()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, initial_length, expected_result', [
            (0, 1, 4, 3),
            (1, 2, 4, 3),
            (1, 3, 4, 2),
            (1, 4, 4, 1),
        ]
    )
    def test__get_effective_first_element_index(self, index_after_last_element, size, initial_length,  expected_result):
        array_queue = ArrayDeque(initial_length=initial_length)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        actual_result = array_queue._get_effective_first_element_index()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, initial_length', [
            (0, 0, 4),
        ]
    )
    def test__get_effective_first_element_index_if_array_is_empty_should_rise_exception(
            self,
            index_after_last_element,
            size,
            initial_length,
    ):
        array_queue = ArrayDeque(initial_length=initial_length)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        with pytest.raises(EmptyCollection):
            array_queue._get_effective_first_element_index()

    @pytest.mark.parametrize(
        'index_after_last_element, size, initial_length', [
            (0, 0, 4),
        ]
    )
    def test__get_effective_last_element_index_if_array_is_empty_should_rise_exception(
            self,
            index_after_last_element,
            size,
            initial_length,
    ):
        array_queue = ArrayDeque(initial_length=initial_length)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        with pytest.raises(EmptyCollection):
            array_queue._get_effective_last_element_index()

    @pytest.mark.parametrize(
        'index_after_last_element, size, initial_length, expected_result', [
            (0, 1, 4, 3),
            (1, 2, 4, 0),
            (1, 3, 4, 0),
            (1, 4, 4, 0),
            (3, 4, 4, 2),
        ]
    )
    def test__get_effective_last_element_index(self, index_after_last_element, size, initial_length, expected_result):
        array_queue = ArrayDeque(initial_length=initial_length)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        actual_result = array_queue._get_effective_last_element_index()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, array, element, expected_result', [
            (0, 1, [None, None, None, '1'], 'element_to_add', {
                '_index_after_last_element': 0,
                '_size': 2,
                '_array': [None, None, 'element_to_add', '1']}
             ),
            (0, 0, [None, None, None, None], 'element_to_add', {
                '_index_after_last_element': 1,
                '_size': 1,
                '_array': ['element_to_add', None, None, None]}
             ),
            (3, 0, [None, None, None, None], 'element_to_add', {
                '_index_after_last_element': 0,
                '_size': 1,
                '_array': [None, None, None, 'element_to_add']}
             ),
            (3, 3, ['1', '2', '3', None], 'element_to_add', {
                '_index_after_last_element': 3,
                '_size': 4,
                '_array': ['1', '2', '3', 'element_to_add']}
             ),
            (3, 4, ['1', '2', '3', '4'], 'element_to_add', {
                '_index_after_last_element': 4,
                '_size': 5,
                '_array': ['4', '1', '2', '3', None, None, None, 'element_to_add']}
             ),
        ]
    )
    def test_add_first(self, index_after_last_element, size, array, element,  expected_result):
        array_queue = ArrayDeque(array=array)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        array_queue.add_first(element)
        actual_result = array_queue.to_dict()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, array, element, expected_result', [
            (0, 0, [None, None, None, None], 'element_to_add', {
                '_index_after_last_element': 1,
                '_size': 1,
                '_array': ['element_to_add', None, None, None]}
             ),
            (0, 1, [None, None, None, '1'], 'element_to_add', {
                '_index_after_last_element': 1,
                '_size': 2,
                '_array': ['element_to_add', None, None, '1']}
             ),
            (3, 1, [None, None, '1', None], 'element_to_add', {
                '_index_after_last_element': 0,
                '_size': 2,
                '_array': [None, None, '1', 'element_to_add']}
             ),
            (3, 3
             , ['1', '2', '3', None], 'element_to_add', {
                '_index_after_last_element': 0,
                '_size': 4,
                '_array': ['1', '2', '3', 'element_to_add']}
             ),
            (3, 4, ['1', '2', '3', '4'], 'element_to_add', {
                '_index_after_last_element': 5

                ,
                '_size': 5,
                '_array': ['4', '1', '2', '3', 'element_to_add'
                    , None, None, None]}
             ),
        ]
    )
    def test_add_last(self, index_after_last_element, size, array, element,  expected_result):
        array_queue = ArrayDeque(array=array)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        array_queue.add_last(element)
        actual_result = array_queue.to_dict()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, array, expected_result', [
            (1, 1, ['element_to_return', None, None, None], 'element_to_return'),
        ]
    )
    def test_first(self, index_after_last_element, size, array,  expected_result):
        array_queue = ArrayDeque(array=array)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        actual_result = array_queue.first()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'index_after_last_element, size, array, expected_result', [
            (1, 1, ['element_to_return', None, None, None], 'element_to_return'),
        ]
    )
    def test_last(self, index_after_last_element, size, array, expected_result):
        array_queue = ArrayDeque(array=array)
        array_queue._index_after_last_element = index_after_last_element
        array_queue._size = size
        actual_result = array_queue.last()
        assert actual_result == expected_result


class TestLeakyStack:
    DEFAULT_LIMIT_OPERATION = 8
    OPERATION_VALUE = 'operation'

    @pytest.mark.parametrize(
        'limit_operation, operation_array, expected_result', [
            (
                    DEFAULT_LIMIT_OPERATION, list(), {
                        '_operations': [None] * DEFAULT_LIMIT_OPERATION,
                        '_size': 0,
                        '_index_of_next_operation': 0,
                    },
            ),
            (
                    DEFAULT_LIMIT_OPERATION, [1], {
                        '_operations': [1],
                        '_size': 0,
                        '_index_of_next_operation': 0,
                    },
            ),
            (
                    DEFAULT_LIMIT_OPERATION, [1, 2], {
                        '_operations': [1, 2],
                        '_size': 0,
                        '_index_of_next_operation': 0,
                    },
            )
        ]
    )
    def test___init__(self, limit_operation, operation_array, expected_result):
        stack = LeakyStack(limit_operations=limit_operation, operation_array=operation_array)
        actual_result = stack.__dict__
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'operation, array_operation, size, index_of_next_operation, expected_result', [
            (
                    OPERATION_VALUE,
                    [None, None, None],
                    0,
                    0, {
                        '_operations': [OPERATION_VALUE, None, None],
                        '_size': 1,
                        '_index_of_next_operation': 1,
                    },
            ),
            (

                    OPERATION_VALUE,
                    [1, None, None],
                    1,
                    1, {
                        '_operations': [1, OPERATION_VALUE, None],
                        '_size': 2,
                        '_index_of_next_operation': 2,
                    },
            ),
            (
                    OPERATION_VALUE,
                    [1, 2, None],
                    2,
                    2, {
                        '_operations': [1, 2, OPERATION_VALUE],
                        '_size': 3,
                        '_index_of_next_operation': 0,
                    },
            ),
            (
                    OPERATION_VALUE,
                    [1, 2, 3],
                    3,
                    0, {
                        '_operations': [OPERATION_VALUE, 2, 3],
                        '_size': 3,
                        '_index_of_next_operation': 1,
                    },
            )
        ]
    )
    def test_add_operation(self, operation, array_operation, size, index_of_next_operation, expected_result):
        stack = LeakyStack(operation_array=array_operation)
        stack._size = size
        stack._index_of_next_operation = index_of_next_operation

        stack.add_operation(operation)
        actual_result = stack.__dict__
        assert actual_result == expected_result

    def test_get_last_operation__raise_exception_when_empty(self):
        stack = LeakyStack()
        with pytest.raises(EmptyCollection):
            stack.get_last_operation()

    @pytest.mark.parametrize(
        'array_operation, size, index_of_next_operation, expected_state, expected_result', [
            (
                    [1, None, None],
                    1,
                    1, {
                        '_operations': [None, None, None],
                        '_size': 0,
                        '_index_of_next_operation': 0,
                    },
                    1
            ),
            (
                    [1, 2, None],
                    2,
                    2, {
                        '_operations': [1, None, None],
                        '_size': 1,
                        '_index_of_next_operation': 1,
                    },
                    2,
            ),
            (
                    [1, 2, 3],
                    3,
                    0, {
                        '_operations': [1, 2, None],
                        '_size': 2,
                        '_index_of_next_operation': 2,
                    },
                    3
            ),
            (
                    [OPERATION_VALUE, 2, 3],
                    3,
                    1, {
                        '_operations': [None, 2, 3],
                        '_size': 2,
                        '_index_of_next_operation': 0,
                    },
                    OPERATION_VALUE,
            )
        ]
    )
    def test_get_last_operation(
            self,
            array_operation,
            size,
            index_of_next_operation,
            expected_state,
            expected_result,
    ):
        stack = LeakyStack(operation_array=array_operation)
        stack._size = size
        stack._index_of_next_operation = index_of_next_operation

        actual_result = stack.get_last_operation()
        actual_state = stack.__dict__
        assert actual_result == expected_result
        assert actual_state == expected_state


class TestPostfixNotationCalculator:
    @pytest.mark.parametrize(
        'expression, expected_result', [
            (['2', '5', '+'], 7.0),
            (['2', '3', '*', '7', '+'], 13.0)
        ]
    )
    def test_calculate(self, expression: List[str], expected_result):
        actual_result = PostfixNotationCalculator(expression).calculate()
        assert actual_result == expected_result
