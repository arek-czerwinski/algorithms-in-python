
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
        self._data = []                       # nonpublic list instance
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
        self._data.append(e)                  # new item stored at end of list

    def _is_stack_full(self):
        if self._maxlen is not None and len(self._data) + 1 > self._maxlen:
            raise FullException(f'The stack is full. It has {len(self._data)} elements.')

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[-1]                 # the last item in the list

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
    def __init__(self, maxlen: int=1):
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
        return self._data[self._top_of_stack_index - 1]                 # the last item in the list

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
    j = raw.find('<')               # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1)        # find next '>' character
        if k == -1:
            return False                # invalid tag
        # tag = raw[j+1:k]              # strip away < >
        tag = _get_tag_name(raw_tag=raw[j+1: k])
        if not tag:
            return False
        if not tag.startswith('/'):   # this is opening tag
            stack.push(tag)
        else:                         # this is closing tag
            if stack.is_empty():
                return False              # nothing to match with
            if tag[1:] != stack.pop():
                return False              # mismatched delimiter
        j = raw.find('<', k+1)        # find next '<' character (if any)
    return stack.is_empty()             # were all opening tags matched?


def _get_tag_name(raw_tag: str):
    raw_tags = [
        part_of_raw_tag
        for part_of_raw_tag in raw_tag.split(sep=' ')
        if part_of_raw_tag and '="' not in part_of_raw_tag
    ]

    return raw_tags[0] if raw_tags else None
