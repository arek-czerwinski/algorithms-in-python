import pytest

from chapter_4.exercises import find_maximum, calculate_recursive_power, reverse, PermutationSolver, \
    calculate_fast_recursive_power, calculate_harmonic_number, string_to_integer, find_max_and_min, \
    find_logarithm_integer_part, solve_uniqueness_problem, calculate_product, solve_hanoi_towers_problem, \
    find_unique_subsets, produce_binary_reprezentation_from_0_to_n, reverse_separated_elements, is_palindrome_recursive, \
    is_more_vowels_in_string, swap_even_numbers_before_odd_numbers, find_pair_number_to_get_sum


# R-4.1
class TestMaximumElementInSequence:
    @pytest.mark.parametrize('input, expected_result', [
        ([2], 2),
        ([1, 2, 3], 3),
        ([3, 2, 4], 4),
        ([-5, -6, -7], -5),
        ([-5, -4, -3, -2, -1, 0], 0),
    ])
    def test_find_maximum(self, input, expected_result):
        assert find_maximum(input) == expected_result

    def test_find_maximum_with_empty_list__failure(self):
        with pytest.raises(ValueError):
            find_maximum(integers=list())


class TestRecursivePower:
    # R-4.2
    @pytest.mark.parametrize('base, power, expected_result', [
        (0, 1, 0),
        (0, 2, 0),
        (1, 0, 1),
        (1, 1, 1),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 4),
        (2, 3, 8),
        (2, 4, 16),
        (2, 5, 32),
        (2, 10, 1024),
    ])
    def test_recursive_power(self, base, power, expected_result):
        assert calculate_recursive_power(base=base, power=power) == expected_result

    # R-4.3
    @pytest.mark.parametrize('base, power, expected_result', [
        (0, 1, 0),
        (0, 2, 0),
        (1, 0, 1),
        (1, 1, 1),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 4),
        (2, 3, 8),
        (2, 4, 16),
        (2, 5, 32),
        (2, 10, 1024),
    ])
    def test_calculate_fast_recursive_power(self, base, power, expected_result):
        assert calculate_fast_recursive_power(base=base, power=power) == expected_result


# R-4.3
class TestReverseFunction:
    # R-4.3
    @pytest.mark.parametrize(
        'input_data, expected_result', [
            ([], []),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([1, 2, 3], [3, 2, 1]),
            ([1, 2, 3, 4], [4, 3, 2, 1]),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ])
    def test_reverse_collection(self, input_data, expected_result):
        assert reverse(objects=input_data) == expected_result


# R-4.5
class TestPermutationSolver:
    @pytest.mark.parametrize(
        'elements, deep_level, expected_result', [
            ([], None, []),
            (['a'], None, [tuple(['a'])]),
            (['a', 'b'], 2, [tuple(['a', 'b']), tuple(['b', 'a'])]),
            (['a', 'b', 'c'], None, [
                ('a', 'b', 'c'),
                ('a', 'c', 'b'),
                ('b', 'a', 'c'),
                ('b', 'c', 'a'),
                ('c', 'a', 'b'),
                ('c', 'b', 'a')
            ])
        ]
    )
    def test__calculate_permutations(self, elements, deep_level, expected_result):
        permutation_solver = PermutationSolver(elements=elements, deep_level=deep_level)
        assert permutation_solver.calculate_permutations() == expected_result

    @pytest.mark.parametrize(
        'elements, expression_to_find, expected_result', [
            (['a', 'b'], ('a',), False),
            (['a', 'b'], ('a', 'b'), True),
            (['a', 'b', 'c'], ('c', 'b', 'a'), True),
            (['a', 'b', 'c'], ('a', 'b', 'c'), True),
            (['a', 'b', 'c'], ('c', 'd', 'a'), False),
            (['a', 'b', 'c'], ('c', 1, 'a'), False),
        ]
    )
    def test_is_belong_to_permutations(self, elements, expression_to_find, expected_result):
        permutation_solver = PermutationSolver(elements=elements)
        assert permutation_solver.check_existence_in_permutation_set(value=expression_to_find) == expected_result


# R-4.6
class TestCalculateHarmonicNumberFunction:
    @pytest.mark.parametrize(
        'maximum, expected_result', [
            (1, 1.0),
            (2, 1.0 + 1 / 2),
            (3, 1.0 + 1 / 2 + 1 / 3),
            (4, 1.0 + 1 / 2 + 1 / 3 + 1 / 4),
            (5, 1.0 + 1 / 2 + 1 / 3 + 1 / 4 + 1 / 5),
        ]
    )
    def test_calculate_harmonic_number(self, maximum, expected_result):
        assert calculate_harmonic_number(how_many_numbers=maximum) == expected_result


# R-4.7
class TestStringToIntegerFunction:
    @pytest.mark.parametrize(
        'string_value, expected_result', [
            ('0', 0),
            ('00', 0),
            ('1', 1),
            ('10', 10),
            ('11', 11),
            ('010', 10),
            ('2333', 2333)
        ]
    )
    def test_string_to_integer(self, string_value, expected_result):
        assert string_to_integer(value=string_value) == expected_result


# C-4.9
class TestFindMaxAndMinFunction:
    @pytest.mark.parametrize(
        'objects, expected_max_min', [
            ([1], (1, 1)),
            ([-1], (-1, -1)),
            ([1, 2], (2, 1)),
            ([1, 2, 3], (3, 1)),
            ([-2, -1, 0], (0, -2))
        ]
    )
    def test_find_min_max(self, objects, expected_max_min):
        assert find_max_and_min(objects) == expected_max_min

    @pytest.mark.parametrize(
        'input', [
            None,
            [],
        ]
    )
    def test_find_min_max_failure(self, input):
        with pytest.raises(ValueError):
            find_max_and_min(collection_of_objs=input)


# C-4.10
class TestFindLogarithmIntegerPartFunction:
    @pytest.mark.parametrize(
        'base, result, expected_result', [
            (100, 1, 0),
            (100, 100, 1),
            (1, 1, 1),
            (2, 2, 1),
            (2, 4, 2),
            (10, 100, 2),
            (10, 1000, 3),
            (3, 9, 2),
            (3, 27, 3),
            (2, 3, 1),
            (3, 4, 1)
        ]
    )
    def test_find_logarithm_integer_part(self, base, result, expected_result):
        assert find_logarithm_integer_part(base=base, result=result) == expected_result

    @pytest.mark.parametrize(
        'base, result', [
            (0, 1),
            (-1, 0)
        ]
    )
    def test_find_logarithm_integer_part_failure(self, base, result):
        with pytest.raises(ValueError):
            find_logarithm_integer_part(base=base, result=result)


# C-4.11
class TestSolveUniquenessProblemFunction:
    @pytest.mark.parametrize(
        'input_data, expected_result', [
            ([], set()),
            ([1], set()),
            ([1, 1], {1}),
            ([1, 2, 1], {1}),
            ([1, 2, 3, 4, 4, 1], {1, 4})
        ]
    )
    def test_solve_uniqueness_problem(self, input_data, expected_result):
        assert solve_uniqueness_problem(data=input_data) == expected_result


# C-4.12
class TestCalculateProductFunction:
    @pytest.mark.parametrize(
        'number1, number2, expected_result', [
            (0, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (1, 1, 1),
            (2, 1, 2),
            (2, 2, 4),
            (2, 3, 6),
            (2, 10, 20),
            (3, 3, 9),
            (1000, 100, 100000)
        ]
    )
    def test_calculate_product(self, number1, number2, expected_result):
        assert calculate_product(number1=number1, number2=number2) == expected_result


# C-4.14
class TestSolveHanoiTowersProblemFunction:
    @pytest.mark.parametrize(
        'source, expected_result', [
            ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([1, 2, 3, 4], [1, 2, 3, 4])
        ]
    )
    def test_solve_hanoi_towers_problem(self, source, expected_result):
        destination = list()
        solve_hanoi_towers_problem(source=source, auxilary=list(), destination=destination)
        print(destination)
        assert destination == expected_result


# C-4.15
class TestFindUniqueSubsets:
    @pytest.mark.parametrize(
        'elements, expected_result', [
            (set(), [set()]),
            ({1}, [set(), {1}]),
            ({1, 2}, [set(), {2}, {1}, {1, 2}]),
            ({1, 2, 3}, [set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]),
        ]
    )
    def test_find_unique_subsets(self, elements: set, expected_result: list):
        actual_result = find_unique_subsets(elements=elements)
        assert list(actual_result) == expected_result

    @pytest.mark.parametrize(
        'n, expected_result', [
            (0, []),
            (1, [(0,), (1,)]),
            (2, [(0, 0), (0, 1), (1, 0), (1, 1)])
        ]
    )
    def test_produce_binary_from_0_to_n(self, n, expected_result):
        actual_result = produce_binary_reprezentation_from_0_to_n(n)
        assert actual_result == expected_result


# C-4.16
class TestReverseSeparatedElements:
    @pytest.mark.parametrize(
        'text, separator, expected_result', [
            ('', ' ', ''),
            ('a', '&', 'a'),
            ('ab', '&', 'ba'),
            ('abc&', '&', 'cba'),
            ('abc&a', '&', 'a&cba'),
            ('&a', '&', 'a'),
            ('ab&cd&ef', '&', 'fe&dc&ba'),
        ]
    )
    def test_reverse_separated_elements_(self, text, separator, expected_result):
        actual_result = reverse_separated_elements(text=text, separator=separator)
        assert actual_result == expected_result


# C-4.17
class TestIsPalindrmeRecursive:
    @pytest.mark.parametrize(
        'text, expected_result', [
            ('', False),
            ('a', True),
            ('ab', False),
            ('aa', True),
            ('aaa', True),
            ('aba', True),
            ('baa', False),
            ('gohangasalamiimalasagnahog', True),
            ('racecar', True),
            ('rakecar', False)
        ]
    )
    def test_is_palindrome_recursive(self, text, expected_result):
        actual_result = is_palindrome_recursive(text=text)
        assert actual_result == expected_result


# C-4.18
class TestIsMoreVowelsInString:
    @pytest.mark.parametrize(
        's, expected_result', [
            ('', False),
            ('a', True),
            ('ab', False),
            ('aa', True),
            ('aaa', True),
            ('aba', True),
            ('baa', True),
            ('aedb', False),
            ('aeub', True),
        ]
    )
    def test_is_more_vowels_in_string(self, s, expected_result):
        actual_result = is_more_vowels_in_string(s=s)
        assert actual_result == expected_result


# C-4.19
class TestSwapEvenNumbersBeforeOddNumbers:
    @pytest.mark.parametrize(
        'numbers, expected_result', [
            ([], []),
            ([1], [1]),
            ([2], [2]),
            ([1, 2], [2, 1]),
            ([2, 1], [2, 1]),
            ([1, 2, 3], [2, 1, 3]),
            ([2, 2, 2], [2, 2, 2]),
            ([1, 1, 1], [1, 1, 1]),
            ([1, 3, 5, 4], [4, 3, 5, 1]),
            ([1, 3, 2, 5], [2, 3, 1, 5]),
            ([1, 3, 2, 4, 5], [2, 4, 1, 3, 5]),
        ]
    )
    def test_swap_even_numbers_before_odd_numbers(self, numbers, expected_result):
        actual_result = swap_even_numbers_before_odd_numbers(numbers)
        assert actual_result == expected_result


class TestFindPairNumbersToGetSum:
    @pytest.mark.parametrize(
        'sorted_numbers, sum_result, expected_result', [
            ([], 5, tuple()),
            ([1], 1, tuple()),
            ([1, 2], 3, tuple([1, 2])),
            ([1, 2, 3], 3, tuple([1, 2])),
            ([1, 2, 3], 4, tuple([1, 3])),
            ([1, 2, 3, 4, 5, 6], 6,  tuple([1, 5])),
        ]
    )
    def test_find_pair_number_to_get_sum(
            self,
            sorted_numbers,
            sum_result,
            expected_result
    ):
        actual_result = find_pair_number_to_get_sum(
            sorted_numbers=sorted_numbers,
            sum_result=sum_result
        )
        assert actual_result == expected_result
