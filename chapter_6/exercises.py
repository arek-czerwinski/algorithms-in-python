import collections

# R-6.1 What values are returned during the following series of stack operations, if
# executed upon an initially empty stack? push(5), push(3), pop(), push(2),
# push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
# pop(), push(4), pop(), pop().
# ====================== SOLUTION ==============================
# push(5), [5]
# push(3), [5, 3]
# pop(),   [5] => 3
# push(2), [5, 2]
# push(8), [5, 2, 8]
# pop(),   [5, 2 ] => 8
# pop(),   [5] => 2
# push(9), [5, 9]
# push(1), [5, 9, 1]
# pop(),   [5, 9, ] => 1
# push(7), [5, 9, 7]
# push(6), [5, 9, 7, 6]
# pop(),   [5, 9, 7 ] => 6
# pop(),   [5, 9 ] => 7
# push(4), [5, 9, 4 ]
# pop(),   [5, 9] => 4
# pop()    [5, ] => 9

# R-6.2 Suppose an initially empty stack S has executed a total of 25 push opera-
# tions, 12 top operations, and 10 pop operations, 3 of which raised Empty
# errors that were caught and ignored. What is the current size of S?

# ================ SOLUTION =============
# (
#   25 push operations - 10 pop operation
#   - 0(top operations ignored) - 0 (error operations ignored)
# ) = 15 elements on stack

# R-6.3 Implement a function with signature transfer(S, T) that transfers all ele-
# ments from stack S onto stack T, so that the element that starts at the top
# of S is the first to be inserted onto T, and the element at the bottom of S
# ends up at the top of T.
from typing import List, Tuple, Any, Dict, Optional, Callable

from utils.errors import EmptyCollection


def transfer_from_stack_to_stack(stack_a: list, stack_b: list):
    while stack_a:
        stack_b.append(stack_a.pop())


# R-6.4 Give a recursive method for removing all the elements from a stack.
def remove_all_elements_from_stack(stack: list):
    if stack:
        stack.pop()
        return remove_all_elements_from_stack(stack=stack)
    else:
        return stack


# R-6.5 Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order.
def reverse(elements: list):
    result = list()
    transfer_from_stack_to_stack(stack_a=elements, stack_b=result)

    return result


# R-6.6 Give a precise and complete definition of the concept of matching for
# grouping symbols in an arithmetic expression. Your definition may be
# recursive.
class ArithmeticGroupingSymbolValidator:
    def __init__(self, left_grouping_symbols, right_grouping_symbols) -> None:
        assert len(left_grouping_symbols) == len(right_grouping_symbols), 'Different size of symbols'
        assert len(set(left_grouping_symbols)) == len(set(right_grouping_symbols)), 'Passed twice the same symbol'

        self._left_grouping_symbols = left_grouping_symbols
        self._right_grouping_symbols = right_grouping_symbols
        self._equivalent = {
            self._right_grouping_symbols[index]: self._left_grouping_symbols[index]
            for index in range(len(self._right_grouping_symbols))
        }

    def valid_arithmetic_grouping(self, arithmetic_expression):
        if not arithmetic_expression:
            return False

        def valid_grouping_symbols(symbol_stack: list, splitted_expression: list):
            if not splitted_expression:
                return symbol_stack
            first_expression, *rest = splitted_expression

            if first_expression in self._left_grouping_symbols:
                symbol_stack.append(first_expression)
            if first_expression in self._right_grouping_symbols:
                if not symbol_stack:
                    raise ValueError(f'{first_expression} not found on last element in stack')
                *rest_stack, last_element = symbol_stack
                symbol_equivalent = self._equivalent[first_expression]
                if last_element == symbol_equivalent:
                    return valid_grouping_symbols(symbol_stack=rest_stack, splitted_expression=rest)

            return valid_grouping_symbols(symbol_stack=symbol_stack, splitted_expression=rest)

        try:
            stack = valid_grouping_symbols(symbol_stack=list(), splitted_expression=arithmetic_expression)
            return False if stack else True
        except ValueError:
            return False


# R-6.7 What values are returned during the following sequence of queue operations,
# if executed on an initially empty queue?
# enqueue(5), [5]
# enqueue(3), [5, 3]
# dequeue(),  [3] => 5
# enqueue(2), [3, 2]
# enqueue(8), [3, 2, 8]
# dequeue(),  [2, 8] => 3
# dequeue(),  [8] => 2
# enqueue(9), [8, 9]
# enqueue(1), [8, 9, 1]
# dequeue(),  [9, 1] => 8
# enqueue(7), [9, 1, 7]
# enqueue(6), [9, 1, 7, 6]
# dequeue(),  [1, 7, 6] => 9
# dequeue(),  [7, 6] => 1
# enqueue(4), [7, 6, 4]
# dequeue(),  [6, 4] => 7
# dequeue().  [4] => 4


# R- 6.8 Suppose an initially empty queue Q has executed a total of 32 enqueue operations,
# 10 first operations, and 15 dequeue operations, 5 of which raised Empty errors that were caught and ignored.
# What is the current size of Q?
# Answer -> Assumption is that, dequeue operation caused those exception.
#  As a result current size is 22
#

# R- 6.9 Had the queue of the previous problem been an instance of ArrayQueue
# that used an initial array of capacity 30, and had its size never been greater than 30,
# what would be the final value of the   front instance variable?
# Answer -> position number 0


# R-6.10 Consider what happens if the loop in the ArrayQueue. resize method at lines 53–55 of
# Code Fragment 6.7 had been implemented as:
# for k in range(self. size):
# self. data[k] = old[k] # rather than old[walk]
# Give a clear explanation of what could go wrong.
# The order should be kept because it is FIFO queue


# R-6.11
# Give a simple adapter that implements our queue ADT while using a collections.deque
# instance for storage.
class MyQueue:
    def __init__(self, elements=tuple()) -> None:
        self._queue = collections.deque(elements)

    def enqueue(self, element):
        self._queue.append(element)

    def dequeue(self):
        return self._queue.pop()

    def first(self):
        first_element = self._queue.popleft()
        self._queue.appendleft(first_element)
        return first_element

    def is_empty(self):
        return len(self._queue) == 0


# R-6.12 WhatvaluesarereturnedduringthefollowingsequenceofdequeADTop-
#  erations, on initially empty deque?
# empty []
# add first(4), [4]
# add last(8),  [4, 8]
# add last(9),  [4, 8, 9]
# add first(5), [5, 4, 8, 9]
# last(),       [5, 4, 8, 9] => 9
# delete first(), [5, 4, 8, 9] => 5
# delete last(),  [5, 4, 8,] => 9
# add last(7),  [5, 4, 8, 7]
# first(),  [5, 4, 8, 7] => 5
# last(),   [5, 4, 8, 7] => 7
# add last(6), [5, 4, 8, 7, 6]
# delete first(),  [4, 8, 7, 6] => 5
# delete first(). [8, 7, 6] => 4


# C-6.15 Suppose Alice has picked three distinct integers and placed them into a stack S in random order.
#  Write a short, straight-line piece of pseudo-code (with no loops or recursion)
# that uses only one comparison and only one variable x, yet that results in variable x storing
# the largest of Alice’s three integers with probability 2/3. Argue why your method is correct.
stack_of_three_numbers = [2, 3, 4]
x = stack_of_three_numbers.pop()
x = x if x > stack_of_three_numbers[0] else stack_of_three_numbers.pop()


# Probability 2/3 occurs because there are three numbers which are all possibilities.
# For this task we can take only two numbers and each pick is independent from each other and this
# is the reason why the probability is 2/3.


class EmptyException(Exception):
    pass


class FullException(Exception):
    pass


class ArrayStackWithMaxLen:
    """LIFO Stack implementation using a Python list as underlying storage."""

    # C - 6.16 Modify the ArrayStack implementation so that the stack’s capacity is limited
    # to maxlen elements, where maxlen is an optional parameter to the constructor
    # (that defaults to None). If push is called when the stack is at full capacity,
    # throw a Full exception (defined similarly to Empty).
    def __init__(self, maxlen=None):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance
        self._maxlen = maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    # C - 6.16
    def push(self, e):
        """Add element e to the top of the stack."""
        self._is_stack_full()
        self._data.append(e)  # new item stored at end of list

    def _is_stack_full(self):
        if self._maxlen is not None and len(self._data) + 1 > self._maxlen:
            raise FullException(f'The stack is full. It has {len(self._data)} elements.')

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data.pop()


# C-6.17 n the previous exercise, we assume that the underlying list is initially empty.
# Redo that exercise,
# this time preallocating an underlying list with length equal to the stack’s maximum capacity.
class ArrayStackWithInitialization:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen: int = 1):
        """Create an empty stack."""
        self._data = [None] * maxlen
        self._top_of_stack_index = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._top_of_stack_index == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._raise_error_if_stack_is_full()
        self._data[self._top_of_stack_index] = e
        self._top_of_stack_index += 1

    def _raise_error_if_stack_is_full(self):
        if len(self._data) == self._top_of_stack_index:
            raise FullException(
                f'The stack is full. It has {len(self._data)} elements. '
                f'Current index is {self._top_of_stack_index}.'
            )

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[self._top_of_stack_index - 1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        popped_value = self._data[self._top_of_stack_index - 1]
        self._data[self._top_of_stack_index - 1] = None
        self._top_of_stack_index -= 1
        return popped_value


# C-6.18 Show how to use the transfer function, described in Exercise R-6.3,
# and two temporary stacks, to replace the contents of a given stack S with those same elements,
# but in reversed order.
def reverse_values_in_stack(stack: list):
    stack_a = list()
    stack_b = list()
    transfer_from_stack_to_stack(stack_a=stack, stack_b=stack_a)
    transfer_from_stack_to_stack(stack_a=stack_a, stack_b=stack_b)
    stack.clear()
    transfer_from_stack_to_stack(stack_a=stack_b, stack_b=stack)

    return stack


# C-6.19 In Code Fragment 6.5 we assume that opening tags in HTML have form <name>, as with <li>.
# More generally, HTML allows optional attributes to be expressed as part of an opening tag.
# The general form used is <name attribute1="value1" attribute2="value2">; for example,
# a table can be given a border and additional padding by using an opening tag of
# <table border="3" cellpadding="5">. Modify Code Frag- ment 6.5 so that it can properly match tags,
#  even when an opening tag may include one or more such attributes.
def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    stack = ArrayStackWithMaxLen()
    j = raw.find('<')  # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        # tag = raw[j+1:k]              # strip away < >
        tag = _get_tag_name(raw_tag=raw[j + 1: k])
        if not tag:
            return False
        if not tag.startswith('/'):  # this is opening tag
            stack.push(tag)
        else:  # this is closing tag
            if stack.is_empty():
                return False  # nothing to match with
            if tag[1:] != stack.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k + 1)  # find next '<' character (if any)
    return stack.is_empty()  # were all opening tags matched?


def _get_tag_name(raw_tag: str):
    raw_tags = [
        part_of_raw_tag
        for part_of_raw_tag in raw_tag.split(sep=' ')
        if part_of_raw_tag and '="' not in part_of_raw_tag
    ]

    return raw_tags[0] if raw_tags else None


# def calculate_non_recursive_combinations(numbers: List[int], is_unique_permutations=False):
#     stack = list()
#     stack.append(numbers)
#     permutations = list()
#
#     while stack:
#         current_element = stack.pop()
#         if current_element:
#             permutations.append(current_element)
#             for index in range(len(current_element)):
#                 sub_element_left = current_element[:index]
#                 sub_element_right = current_element[index+1:]
#                 stack.append(sub_element_left)
#                 stack.append(sub_element_right)
#
#     if is_unique_permutations:
#         return list(set(permutations))
#     return permutations


def shift_numbers(numbers, shift_index):
    left_numbers = numbers[:shift_index]
    right_numbers = numbers[shift_index:]
    shifted_numbers = right_numbers + left_numbers
    return tuple(shifted_numbers)


# def permute_with_stack(numbers: List[int], r=None):
#     pool = tuple(numbers)
#     permutations = tuple()
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n - r, -1))
#     print(f'indices: {indices}, cycles {cycles}')
#     permutations = permutations + (tuple(pool[i] for i in indices[:r]),)
#     while n:
#         print(f'PERMUTATIONS n: {n} : {permutations}')
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             print(f'Changed cycles {cycles}')
#             if cycles[i] == 0:
#                 indices[i:] = indices[i + 1:] + indices[i:i + 1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 permutations = permutations + (tuple(pool[i] for i in indices[:r]),)
#                 break
#         else:
#             print('PERMUTATIONS : ', permutations)
#             return permutations

# def permute_with_stack(numbers: List[int]):
#     if not numbers:
#         return [tuple()]
#     if len(numbers) == 1:
#         return [(1, )]
#     permutations = []
#     for shift_index in range(0, len(numbers)):
#         shifted_numbers = shift_numbers(numbers, shift_index)
#
#         stack = list()
#         for index in range(1, len(shifted_numbers)):
#             stack.append((shifted_numbers[:index], shifted_numbers[index:]))
#
#         print(f'SHIFTED_NUMBERS {shifted_numbers} index: {shift_index}, stack: {stack}')
#         while stack:
#             left_side, right_side = stack.pop()
#             if len(right_side) == 1:
#                 # continue
#                 permutation = left_side + right_side
#                 print(
#                     f'Adding permutation with right size is 1 : {permutation}, left_side:{left_side}, right_side:{right_side}, stack:{stack}',
#                 )
#                 permutations.append(left_side + right_side)
#                 continue
#             for left_side_index in range()
#             for right_sift_index in range(1, len(right_side)):
#                 permutation = left_side + shift_numbers(numbers=right_side, shift_index=right_sift_index)
#                 print(
#                     f'Adding permutation{permutation}, left_side:{left_side}, right_side:{right_side}, stack:{stack}',
#                 )
#                 permutations.append(left_side + shift_numbers(numbers=right_side, shift_index=right_sift_index))
#
#     print('PERMUTATIONS : ', permutations)
#
#     return tuple(set(permutations))


# def permute_with_stack(numbers: List[int]):
#     n = len(numbers)
#     result = []
#     c = n * [0]
#
#     result.append(tuple(numbers))
#
#     i = 0
#     while i < n:
#         if c[i] < i:
#             if i % 2 == 0:
#                 tmp = numbers[0]
#                 numbers[0] = numbers[i]
#                 numbers[i] = tmp
#
#             else:
#
#                 tmp = numbers[c[i]]
#                 numbers[c[i]] = numbers[i]
#                 numbers[i] = tmp
#
#             result.append(tuple(numbers))
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#
#     return result

class PermutationEntry:

    def __init__(self, result: Tuple, permutation_state: Tuple) -> None:
        self._result = result
        self._permutation_state = permutation_state

    @property
    def result(self):
        return self._result

    @property
    def permutation_state(self):
        return self._permutation_state

    def __repr__(self) -> str:
        return f'[result:{self.result}, permutation_state:{self.permutation_state}]'


# C-6.21
# Describe a nonrecursive algorithm for enumerating all permutations of the numbers {1,2,...,n} using an explicit stack.
def permute_with_stack(numbers: Tuple[int]):
    stack = list()
    stack.append(PermutationEntry(result=tuple(), permutation_state=numbers))

    permutations = []

    while stack:
        element_on_top = stack.pop()
        if len(element_on_top.permutation_state) == 0:
            permutations.append(element_on_top.result)
        else:
            for index in range(len(element_on_top.permutation_state)):
                old_result = element_on_top.result
                old_permutation_state = element_on_top.permutation_state
                new_result = old_result + tuple([old_permutation_state[index]])
                permutation_state = (
                        old_permutation_state[0: max(0, index)]
                        + old_permutation_state[index + 1: len(old_permutation_state)]
                )
                stack.append(PermutationEntry(result=new_result, permutation_state=permutation_state))

    return permutations


# C-6.21 Show how to use a stack S and a queue Q to generate all possible subsets of an n-element set T nonrecursively
def get_all_subsets(elements: List[Any]):
    stack = list()
    stack.append(elements)

    subsets = list()
    subsets.append(list())

    while stack and elements:
        top_element = stack.pop()
        subsets.append(top_element)
        if not top_element:
            continue
        else:
            for index in range(len(top_element)):
                new_subset = top_element[:index] + top_element[index + 1:]
                if new_subset:
                    stack.append(new_subset)

    unique_subsets = dict()
    for subset in subsets:
        unique_subsets[tuple(subset)] = subset

    return unique_subsets.values()


# C-6.22
# Postfix notation is an unambiguous way of writing an arithmetic expression without parentheses.
# It is defined so that if “(exp1)op(exp2)” is a normal, fully parenthesized expression whose operation is op,
# the postfix version of this is “pexp1 pexp2 op”,
# where pexp1 is the postfix version of exp1 and pexp2 is the postfix version of exp2.
# The postfix version of a single number or variable is just that number or variable.
# For example, the postfix version of “((5+2)∗(8−3))/4” is “5 2 + 8 3 − ∗ 4 /”.
# Describe a nonrecursive way of evaluating an expression in postfix notation.


ADDITION = '+'
SUBTRACTION = '-'
MULTIPLICATION = '*'
DIVISION = '/'
OPERATORS = tuple([ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION])
OPERATOR_PRIORITIES = {
    ADDITION: 0,
    SUBTRACTION: 0,
    MULTIPLICATION: 1,
    DIVISION: 1,
}
OPEN_PARENTHESIS = tuple(['(', '[', '{'])
CLOSED_PARENTHESIS = tuple([')', ']', '}'])


class ArithmeticExpressionToPostfixExpression:
    def __init__(
            self,
            operators: Tuple[str, ...] = OPERATORS,
            operator_priorities: Dict[str, int] = None,
            open_parenthesis: Tuple[str, ...] = OPEN_PARENTHESIS,
            closed_parenthesis: Tuple[str, ...] = CLOSED_PARENTHESIS,

    ) -> None:
        self._operators = operators
        self._operator_priorities = operator_priorities if operator_priorities else OPERATOR_PRIORITIES
        self._open_parenthesis = open_parenthesis
        self._closed_parenthesis = closed_parenthesis

    def parse(self, expression_elements: str) -> List[Any]:
        if not expression_elements:
            return list()
        expression_elements = [element for element in expression_elements.split(sep=' ') if element]
        postfix_notation = list()
        operators = list()
        for char in expression_elements:
            if char.isdigit():
                postfix_notation.append(float(char))
            elif self._is_operator(char=char):
                operators = self._move_operator_to_postfix_expression_if_needed(
                    current_operand=char,
                    operators=operators,
                    postfix_notation=postfix_notation,
                )
                operators.append(char)
            elif self._is_open_parenthesis(char=char):
                operators.append(char)
            elif self._is_closed_parenthesis(char=char):
                self._move_operator_to_postfix_in_reverse_order_to_first_open_parenthesis(
                    closed_parenthesis=char,
                    postfix_notation=postfix_notation,
                    operators=operators,
                )
            else:
                raise ValueError(f'wrong character {char}!')

        self._move_operator_to_postfix_in_reverse_order(
            postfix_notation=postfix_notation,
            operators=operators,
        )
        return postfix_notation

    def _is_operator(self, char: str):
        return char in self._operators

    def _is_open_parenthesis(self, char: str):
        return char in self._open_parenthesis

    def _is_closed_parenthesis(self, char: str):
        return char in self._closed_parenthesis

    def _move_operator_to_postfix_expression_if_needed(self, current_operand, operators, postfix_notation):
        last_operand = self._find_last_arithmetic_operator_before_first_open_parenthesis(
            operators=operators,
        )
        if last_operand:
            last_operand_priority = self._operator_priorities[last_operand]
            current_operand_priority = self._operator_priorities[current_operand]
            if last_operand_priority > current_operand_priority:
                operators = self._move_operator_to_postfix_in_reverse_order(
                    operators=operators,
                    postfix_notation=postfix_notation,
                )
        return operators

    def _find_open_parenthesis(self, closed_parenthesis: str):
        for index in range(len(self._closed_parenthesis)):
            if self._closed_parenthesis[index] == closed_parenthesis:
                return self._open_parenthesis[index]

        raise ValueError(f'Not known closed parenthesis {closed_parenthesis}!')

    def _find_last_arithmetic_operator_before_first_open_parenthesis(self, operators: List[str]):
        for index in range(len(operators) - 1, -1, -1):
            possible_operator = operators[index]
            if possible_operator in self._operators:
                return possible_operator
            if possible_operator in self._open_parenthesis:
                break
        return None

    def _move_operator_to_postfix_in_reverse_order(
            self,
            postfix_notation: List[Any],
            operators: List[str],
    ):
        while operators:
            operator = operators.pop()
            if (
                    self._is_open_parenthesis(char=operator)
                    or self._is_closed_parenthesis(char=operator)
            ):
                raise ValueError(
                    f'Passed wrong expression! '
                    f'During passing operators to postfix expression found parenthesis {operator}'
                )
            postfix_notation.append(operator)
        return operators

    def _move_operator_to_postfix_in_reverse_order_to_first_open_parenthesis(
            self,
            closed_parenthesis: str,
            postfix_notation: List[Any],
            operators: List[str],
    ):
        closed_parenthesis = self._find_open_parenthesis(closed_parenthesis=closed_parenthesis)
        while operators:
            operator = operators.pop()
            if operator == closed_parenthesis:
                break
            postfix_notation.append(operator)

        return operators


# C-6.23
# Suppose you have three none empty stacks R,S,and T.
# Describe a sequence of operations that results in S storing all elements originally in T below
# all of S’s original elements, with both sets of those elements in their original order.
# The final configuration for R should be the same as its original configuration.
# For example, if R = [1,2,3], S = [4,5], and T = [6,7,8,9], the final configuration should have
# R = [1,2,3] and S = [6,7,8,9,4,5].
def move_elements_stack_t_to_stack_s_with_original_sequence(
        r: List[Any],
        s: List[Any],
        t: List[Any],
):
    copy_r = list(r)
    copy_s = list(s)
    copy_t = list(t)
    size_t = len(t)

    while copy_t:
        copy_r.append(copy_t.pop())

    while copy_s:
        copy_t.append(copy_s.pop())

    while size_t:
        copy_s.append(copy_r.pop())
        size_t -= 1
    while copy_t:
        copy_s.append(copy_t.pop())

    return copy_r, copy_s, copy_t


# C-6.24
# Describe how to implement the stack ADT using a single queue as an instance variable,
# and only constant additional local memory within the method bodies.
# What is the running time of the push(), pop(), and top() methods for your design?
class StackBasedOnQueue:
    def __init__(self):
        self.items = []

    def top(self):  # running time 1
        return self.items.pop()

    def push(self, item):  # running time 1
        self.items.insert(0, item)

    def pop(self):  # running time 1
        return self.top()


# C-6.25
# Describe how to implement the queue ADT using two stacks as instance variables,
# such that all queue operations execute in amortized O(1) time.
# Give a formal proof of the amortized bound.
class SimpleQueueWithTwoStacks:
    def __init__(
            self,
            stack_for_adding_elements: Optional[List[object]] = None,
            stack_for_removing_elements: Optional[List[object]] = None,
    ):
        self._stack_for_adding_elements = stack_for_adding_elements if stack_for_adding_elements else list()
        self._stack_for_removing_elements = stack_for_removing_elements if stack_for_removing_elements else list()

    def enqueue(self, element: object) -> None:
        self._stack_for_adding_elements.append(element)

    def dequeue(self) -> object:
        if len(self) == 0:
            raise ValueError('The queue is empty!')
        if not self._stack_for_removing_elements:
            self.move_elements_to_stack_for_removing()

        return self._stack_for_removing_elements.pop()

    def move_elements_to_stack_for_removing(self):
        while self._stack_for_adding_elements:
            element = self._stack_for_adding_elements.pop()
            self._stack_for_removing_elements.append(element)

    def first(self) -> object:
        if not self._stack_for_adding_elements:
            raise ValueError('The queue is empty!')
        size = len(self._stack_for_adding_elements)
        return self._stack_for_adding_elements[size - 1]

    def is_empty(self) -> bool:
        return not bool(self._stack_for_adding_elements or self._stack_for_removing_elements)

    def __len__(self):
        return len(self._stack_for_adding_elements) + len(self._stack_for_removing_elements)


# C-6.26
# Describe how to implement the double-ended queue ADT using two stacks as instance variables.
# What are the running times of the methods?
# Solution
# Solution is similar like in # C-6.25 with small difference that elements can be moved on both direction

# C-6.27
# Suppose you have a stack S containing n elements and a queue Q that is initially empty.
# Describe how you can use Q to scan S to see if it contains a certain element x, with the additional constraint
# that your algorithm must return the elements back to S in their original order. You may only use S, Q,
# and a constant number of other variables.
def has_element_in_stack(stack: list, element_to_find: object):
    is_found = False
    queue = list()
    while stack:
        current_element = stack.pop()
        queue.append(current_element)
        if current_element == element_to_find:
            is_found = True
            break

    while queue:
        stack.append(queue.pop())

    return is_found


# C-6.28
# Modify the ArrayQueue implementation so that the queue’s capacity is limited to maxlen elements,
# where maxlen is an optional parameter to the constructor (that defaults to None).
# If enqueue is called when the queue is at full capacity, throw a Full exception (defined similarly to Empty).
class ArrayQueue:
    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self, max_length: int = None):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._max_length = max_length or ArrayQueue.DEFAULT_CAPACITY

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyCollection('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise EmptyCollection('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        # added condition for checking max length
        if cap >= self._max_length:
            raise FullException('The collection is full!')
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    # C-6.29
    # In certain applications of the queue ADT, it is common to repeatedly dequeue an element, process
    # it in some way, and then immediately enqueue the same element.
    # Modify the ArrayQueue implementation to include a rotate()
    # method that has semantics identical to the combination, Q.enqueue(Q.dequeue( )).
    # However, your implementation should be more efficient than making two separate calls
    # (for example, because there is no need to modify size).

    # In my opinion there are two possible options
    # 1. rotate function should return first or last element by reference. The client will do something with passed
    # object but still the object will be in queue
    # 2. Other option would be adding additional parameter called do_something which is a function which take one
    # parameter which is element from queue. The function will change something in the stated of passed object and later
    # it will return reference to changed object.
    def rotate_1(self):
        return self.first()

    def rotate_2(self, do_something: Callable):
        element = self._data[self._front]
        processed_element = do_something(element)
        self._data[self._front] = processed_element


# C-6.30
# Alice has two queues, Q and R, which can store integers. Bob gives Alice 50 odd integers and 50 even integers
# and insists that she store all 100 integers in Q and R.
# They then play a game where Bob picks Q or R at random and then applies the round-robin scheduler,
# described in the chapter, to the chosen queue a random number of times.
# If the last number to be processed at the end of this game was odd, Bob wins. Otherwise,
# Alice wins. How can Alice allocate integers to queues to optimize her chances of winning?
# What is her chance of winning?

# Alice should put on an even integer in Q and all the other 99 integers in R.
# The chance that Bob picks Q is 0.5, where Alice must win.
# The chance that Bob pocks R is also 0.5,
# where Alice wins at the chance of 49/99 (49 even integers out of 99 overall integers).
# This gives her 0.5*(1+49/99) = 74/99 chance of winning.


# C-6.31
# Suppose Bob has four cows that he wants to take across a bridge, but only one yoke, which can hold up to two
# cows, side by side, tied to the yoke.
# The yoke is too heavy for him to carry across the bridge, but he can tie (and untie) cows to it in no time at all.
# Of his four cows, Mazie can cross the bridge in 2 minutes,
# Daisy can cross it in 4 minutes,
# Crazy can cross it in 10 minutes, and Lazy can cross it in 20 minutes.
# Of course, when two cows are tied to the yoke, they must go at the speed of the slower cow.
# Describe how Bob can get all his cows across the bridge in 34 minutes.
# The solution is to walk 2 of the fastest cows across the bridge without the yoke.
# 1- So walk Maxie across in 2 minutes.
# 2- Bob walks back to the start in 2 minutes. (
# We can assume that if Bob can walk there in 2 minutes he can also walk back in 2 minutes).
# 3- Bob walks Daisy across in 4 minutes.
# 4 - Bob walks back to the start in 2 minutes.
# 5 - Crazy and Lazy are walked across with the yoke in 20 minutes.


# p-6.32 Give a complete ArrayDeque implementation of the double-ended queue ADT as sketched in Section 6.3.2.
class ArrayDeque:
    def __init__(self, initial_length: int = 16, array: Optional[List[Any]] = None) -> None:
        self._index_after_last_element = 0
        self._size = 0
        self._array = array or [None] * initial_length

    def to_dict(self):
        return {
            '_index_after_last_element': self._index_after_last_element,
            '_size': self._size,
            '_array': self._array,
        }

    def add_first(self, element: Any):
        self._should_copy_elements_from_array_to_new_array()

        index_of_element_to_add = self._get_index_before_first_element()
        self._add_element_to_array(element=element, index=index_of_element_to_add)

        # when an array is empty _index_after_last_element should
        # be increased to point where to add new element in last position
        if len(self) == 1:
            self._increase_index_after_last_element()

    def _should_copy_elements_from_array_to_new_array(self):
        if self._is_array_full():
            new_array = [None] * (self._size * 2)
            self._copy_elements_to_new_array(new_array)
            self._array = new_array
            self._index_after_last_element = self._size

    def _copy_elements_to_new_array(self, new_array):
        first_element_index = self._get_effective_first_element_index()
        for shift in range(self._size):
            effective_index = self._get_effective_index(first_element_index + shift)
            new_array[shift] = self._array[effective_index]

    def _add_element_to_array(self, element: Any, index: int):
        self._array[index] = element
        self._increase_size()

    def _increase_size(self):
        self._size += 1
        if self._size > len(self._array):
            raise FullException(f'Increased size of array to {self._size} but size of array is {len(self._array)}')

    def _increase_index_after_last_element(self):
        self._index_after_last_element = self._get_effective_index(self._index_after_last_element + 1)

    def add_last(self, element):
        self._should_copy_elements_from_array_to_new_array()

        index_of_element_to_add = self._get_index_after_last_element()
        self._add_element_to_array(element=element, index=index_of_element_to_add)
        self._increase_index_after_last_element()

    def delete_first(self):
        pass  # similar like to add first element

    def delete_last(self):
        pass  # similar like to add last element

    def first(self):
        index_of_first_element = self._get_effective_first_element_index()
        return self._array[index_of_first_element]

    def last(self):
        index_of_first_element = self._get_effective_last_element_index()
        return self._array[index_of_first_element]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _is_array_full(self):
        return self._size == len(self._array)

    def _get_index_after_last_element(self):
        return self._index_after_last_element

    def _get_index_before_first_element(self):
        if self.is_empty():
            return self._index_after_last_element
        return self._get_effective_index(self._get_index_after_last_element() - self._size - 1)

    def _get_effective_first_element_index(self):
        self.raise_exception_if_empty()
        return self._get_effective_index((self._get_index_before_first_element() + 1))

    def raise_exception_if_empty(self):
        if self.is_empty():
            raise EmptyCollection('This collection is empty')

    def _get_effective_last_element_index(self):
        self.raise_exception_if_empty()
        return self._get_effective_index(self._get_index_after_last_element() - 1)

    def _get_effective_index(self, index: int):
        return index % len(self._array)
