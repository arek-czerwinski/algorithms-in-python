# R-4.1
# Describe a recursive algorithm for finding the maximum element in a se-
# quence, S, of n elements. What is your running time and space usage?
from itertools import compress, product


def find_maximum(integers):
    """
     running time is n
    """
    if not integers:
        raise ValueError('Parameter numbers should be not empty.')

    def find_maximum_in_collection(numbers, maximum):
        if not numbers:
            return maximum
        if maximum < numbers[0]:
            maximum = numbers[0]
        return find_maximum_in_collection(numbers=numbers[1:], maximum=maximum)

    return find_maximum_in_collection(numbers=integers[1:], maximum=integers[0])


# R-4.2
# Draw the recursion trace for the computation of power(2, 5), using the
# traditional function implemented in Code Fragment 4.11.
def calculate_recursive_power(base, power):
    if base == 0:
        return 0
    if power == 0:
        return 1
    if power == 1:
        return base

    return base * calculate_recursive_power(base=base, power=power - 1)


# R-4.3
# Draw the recursion trace for the computation of power(2, 18), using the
# repeated squaring algorithm, as implemented in Code Fragment 4.12.
def calculate_fast_recursive_power(base, power):
    if base == 0:
        return 0
    if power == 0:
        return 1
    if power == 1:
        return base

    partial = calculate_fast_recursive_power(base=base, power=power // 2)
    result = partial * partial
    if power % 2 == 1:
        result *= base
    return result


# R-4.4
# Draw the recursion trace for the execution of function reverse(S, 0, 5)
# (Code Fragment 4.10) on S = [4, 3, 6, 2, 6].
def reverse(objects):
    def reverse_collection(objects, start, end):
        if start > end:
            return objects
        tmp = objects[start]
        objects[start] = objects[end]
        objects[end] = tmp

        return reverse_collection(objects, start=start + 1, end=end - 1)

    return reverse_collection(objects=objects, start=0, end=len(objects) - 1)


# R-4.5
# Draw the recursion trace for the execution of function PuzzleSolve(3, S,U )
# (Code Fragment 4.14), where S is empty and U = {a, b, c, d}.
class PermutationSolver:
    def __init__(self, elements, deep_level=None):
        self.elements = elements
        if not deep_level:
            self.deep_level = len(self.elements)
        else:
            self.deep_level = deep_level

        self._all_permutations = None

    def calculate_permutations(self):
        _result_of_permutations = []

        def _calculate_permutations(deep: int, result: tuple, elements):
            for index in range(0, len(elements)):
                if deep <= 1:
                    _result_of_permutations.append(result + tuple([elements[index]]))
                else:
                    _calculate_permutations(
                        deep=deep - 1,
                        result=result + tuple(elements[index]),
                        elements=elements[0: max(0, index)] + elements[index + 1: len(elements)]
                    )

        _calculate_permutations(deep=self.deep_level, result=tuple(), elements=self.elements)
        return _result_of_permutations


    def check_existence_in_permutation_set(self, value):
        if not self._all_permutations:
            self._all_permutations = self.calculate_permutations()

        for permutation in self._all_permutations:
            if value == permutation:
                return True
        return False


# R-4.6
# Describe a recursive function for computing the n th Harmonic number
def calculate_harmonic_number(how_many_numbers, sum_of_numbers=0.0):
    if how_many_numbers <= 1:
        return sum_of_numbers + 1.0

    return calculate_harmonic_number(
        how_many_numbers=how_many_numbers - 1,
        sum_of_numbers=sum_of_numbers + (1 / how_many_numbers)
    )


# R-4.7
# Describe a recursive function for converting a string of digits into the in-
# teger it represents. For example, 13531 represents the integer 13, 531.
def string_to_integer(value: str, multiplier=1, sum_of_numbers=0):
    if not value:
        return sum_of_numbers
    return string_to_integer(
        value=value[0:len(value) - 1],
        multiplier=multiplier * 10,
        sum_of_numbers=sum_of_numbers + (int(value[-1]) * multiplier)
    )


# C-4.9
# Write a short recursive Python function that finds the minimum and max-
# imum values in a sequence without using any loops.
def find_max_and_min(collection_of_objs, max_obj=None, min_obj=None):
    if not collection_of_objs:
        raise ValueError('objects can not be None or empty')

    if not max_obj:
        max_obj = collection_of_objs[0]
    if not min_obj:
        min_obj = collection_of_objs[0]

    def _find_max_min(collection, maximum, minimum):
        if len(collection) == 0:
            return maximum, minimum
        else:
            if collection[0] > maximum:
                maximum = collection[0]
            if collection[0] < minimum:
                minimum = collection[0]

            return find_max_and_min(collection_of_objs=collection_of_objs[1:], max_obj=maximum, min_obj=minimum)

    return _find_max_min(collection=collection_of_objs[1:], maximum=max_obj, minimum=min_obj)


# C-4.10
# Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.
def find_logarithm_integer_part(result, base=2):
    if base <= 0:
        raise ValueError('base should not be less or equal 0')
    if base == result:
        return 1
    if result == 1:
        return 0

    # TODO logic should be improved. dirty hacks
    def _find_logarithms_integer_part(_base, _result, ):
        if result < _base:
            return 0
        return 1 + find_logarithm_integer_part(result / base, base=base)

    return _find_logarithms_integer_part(
        _base=base,
        _result=result
    )


# C-4.11
# Describe an efficient recursive function for solving the element unique-
# ness problem, which runs in time that is at most O(n 2 ) in the worst case
# without using sorting.
# =======
# possible solution, hashing, sorting, iteration, recursion
def solve_uniqueness_problem(data: list):
    def is_unique_value(data: list, value):
        if not data:
            return True

        if data[0] == value:
            return False

        return is_unique_value(data=data[1:], value=value)

    not_unique_elements = set()
    for index in range(len(data)):
        if not is_unique_value(data=data[index + 1:], value=data[index]):
            not_unique_elements.add(data[index])

    return not_unique_elements


# C-4.12
# Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.
def calculate_product(number1: int, number2: int):
    if not number1 or not number2:
        return 0

    def _add_base(total_sum, base, how_many_times):
        if how_many_times == 0:
            return total_sum
        return _add_base(total_sum=total_sum + base, base=base, how_many_times=how_many_times - 1)

    return _add_base(total_sum=0, base=number1, how_many_times=number2)


# C-4.13
# In Section 4.2 we prove by induction that the number of lines printed by
# a call to draw interval(c) is 2 c − 1. Another interesting question is how
# many dashes are printed during that process. Prove by induction that the
# number of dashes printed by draw interval(c) is 2 c+1 − c − 2.
# draw_interval(3)
# - draw_interval(2)
# - draw_interval(1)
# - draw_interval(0) = > None
# - draw_line(1) = > -
# - draw_interval(0) = > None
# - draw_line(2) = > --
# - draw_interval(1)
# - draw_interval(0) = > None
# - draw_line(1) = > -
# - draw_interval(0) = > None
# draw_interval(2)
# - draw_interval(1)
# - draw_interval(0) = > None
# - draw_line(1) = > -
# - draw_interval(0) = > None
# - draw_line(2) = > --
# draw_interval(1)
# - draw_interval(0) = > None
# - draw_line(1) = > -
# - draw_interval(0) = > None
#
# draw_interval(c) = > how
# many
# printed
# lines
# 2 ^ ^ (c) - (1)
#
# draw_interval(1) = > 2 - 1 = 1
# draw_interval(2) = > 4 - 1 = 3
# draw_interval(3) = > 8 - 1 = 7
# draw_interval(4) = > 16 - 1 = 16
#
# draw_interbal(c) = > how
# many
# dashes
# printed
# 2 ^ ^ (c + 1) - c - 2
#
# draw_interval(1) = > 2 ^ ^ (1 + 1) - 1 - 2 = 0 == > 2 ^ ^ (c + 1) - c - 2
# draw_interval(2) = > 2 ^ ^ (2 + 1) - 2 - 2 = 4 == > 2 ^ ^ (c + 1) - c - 2
#
# PROOF:
# 1 + 2 * 2 ^ ^ (c) - c - 1 - 2 = 2 ^ ^ (c + 1) + c - 2

# C-4.14
# In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
# b, and c, sticking out of it. On peg a is a stack of n disks, each larger than
# the next, so that the smallest is on the top and the largest is on the bottom.
# The puzzle is to move all the disks from peg a to peg c, moving one disk
# at a time, so that we never place a larger disk on top of a smaller one.
# See Figure 4.15 for an example of the case n = 4. Describe a recursive
# algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint:
# Consider first the subproblem of moving all but the n th disk from peg a to
# another peg using the third as “temporary storage.”)


def solve_hanoi_towers_problem(source, auxilary, destination):
    def _move_disk(how_many_disks, source, auxilary, destination):
        print("source ", source, " auxilary ", auxilary, " destination ", destination)
        if how_many_disks > 0:
            _move_disk(how_many_disks=how_many_disks - 1, source=source, auxilary=destination, destination=auxilary)
            if source:
                print("move disk ", "source ", source, " auxilary ", auxilary, " destination ", destination)
                destination.append(source.pop())
            _move_disk(how_many_disks=how_many_disks - 1, source=auxilary, auxilary=source, destination=destination)

    return _move_disk(how_many_disks=len(source), source=source, auxilary=auxilary, destination=destination)


# C-4.15 Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
def find_unique_subsets(elements: set):
    def _find_unique_subset(items: list):
        if not items:
            return [set()]
        return (set(compress(items, mask)) for mask in product(*[[0, 1]] * len(items)))

    return _find_unique_subset(items=list(elements))


BINARY = [0, 1]


# binary permutations
def produce_binary_reprezentation_from_0_to_n(n):
    if not n:
        return []
    final_result = []

    def produce_binary(n, result: tuple):
        if n == 0:
            final_result.append(result)
            return
        for b in BINARY:
            produce_binary(n=n - 1, result=result + tuple([b]))

        return result

    produce_binary(n, result=tuple())
    return final_result


# def per(n):
#     for i in range(1<<n):
#         s=bin(i)[2:]
#         s='0'*(n-len(s))+s
#         print map(int,list(s))


# C-4.16 Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be
# snap&stop .
def reverse_separated_elements(text: str, separator: str):
    def _reverse_string(s: str):
        return s[::-1]

    def _reverse_separated_elements(separared_text: list):
        if not separared_text:
            return ''
        result = _reverse_separated_elements(separared_text=separared_text[1:])
        if result:
            result = result + separator
        return result + _reverse_string(separared_text[0])

    separared_text = [sub_string for sub_string in text.split(sep=separator) if sub_string]
    return _reverse_separated_elements(separared_text=separared_text)


# C-4.17 Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.
def is_palindrome_recursive(text: str):
    def _is_palindrome_rescursive(s: str, start_index: int, end_index: int):
        if start_index > end_index:
            return True
        if s[start_index] != s[end_index]:
            return False
        return _is_palindrome_rescursive(s=s, start_index=start_index + 1, end_index=end_index - 1)

    if not text:
        return False

    if len(text) == 1:
        return True

    return _is_palindrome_rescursive(s=text, start_index=0, end_index=len(text) - 1)


VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}


# C-4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.
def is_more_vowels_in_string(s: str):
    def _is_more_vowels_in_string(s: str, current_index, how_many_vowels: int):
        if current_index >= len(s):
            if how_many_vowels > len(s) / 2:
                return True
            else:
                return False

        if how_many_vowels > len(s) / 2:
            return True

        current_character = s[current_index]
        if current_character in VOWELS:
            how_many_vowels = how_many_vowels + 1
        return _is_more_vowels_in_string(s=s, current_index=current_index+1, how_many_vowels=how_many_vowels)

    if not s:
        return False

    return _is_more_vowels_in_string(s=s, current_index=0, how_many_vowels=0)


# C-4.19 Write a short recursive Python function that rearranges a sequence of in-
# teger values so that all the even values appear before all the odd values.
def swap_even_numbers_before_odd_numbers(numbers: list):
    numbers_length = len(numbers)

    def _swap_even_numbers_before_odd_numbers(numbers: list, even_index: int, odd_index: int):
        if even_index >= numbers_length or odd_index >= numbers_length:
            return numbers
        if numbers[even_index] % 2 != 0:
            return _swap_even_numbers_before_odd_numbers(numbers=numbers, even_index=even_index+1, odd_index=odd_index)
        if numbers[odd_index] % 2 == 0:
            return _swap_even_numbers_before_odd_numbers(numbers=numbers, even_index=even_index, odd_index=odd_index+1)
        if numbers[even_index] % 2 == 0 and numbers[odd_index] % 2 != 0:
            if even_index > odd_index:
                tmp_even = numbers[even_index]
                numbers[even_index] = numbers[odd_index]
                numbers[odd_index] = tmp_even

            return _swap_even_numbers_before_odd_numbers(numbers=numbers, even_index=even_index, odd_index=odd_index+1)
        raise ValueError('UPS')

    if not numbers or len(numbers) == 1:
        return numbers

    return _swap_even_numbers_before_odd_numbers(numbers=list(numbers), even_index=0, odd_index=0)


def find_pair_number_to_get_sum(sorted_numbers: list, sum_result: int):
    def _find_pair_number_to_get_sum(
            sorted_numbers: list,
            sum_result: int,
            start_index: int,
            end_index: int
    ):
        if start_index > end_index:
            return tuple()
        sum_of_two_numbers = sorted_numbers[start_index] + sorted_numbers[end_index]
        if sum_of_two_numbers == sum_result:
            return sorted_numbers[start_index], sorted_numbers[end_index]
        elif sum_of_two_numbers < sum_result:
            return _find_pair_number_to_get_sum(
                sorted_numbers=sorted_numbers,
                sum_result=sum_result,
                start_index=start_index+1,
                end_index=end_index
            )
        else:
            return _find_pair_number_to_get_sum(
                sorted_numbers=sorted_numbers,
                sum_result=sum_result,
                start_index=start_index,
                end_index=end_index-1
            )

    if not sorted_numbers:
        return tuple()

    return _find_pair_number_to_get_sum(
        sorted_numbers=sorted_numbers,
        sum_result=sum_result,
        start_index=0,
        end_index=len(sorted_numbers) - 1
    )