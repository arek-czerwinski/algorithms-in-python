import functools

import itertools
import pytest

from chapter_1.exercises import *


# R-1.1
class TestIsMultipleFunction:
    def test_m_is_larger_than_n_success(self):
        assert not is_multiple(n=5, m=6)

    def test_m_is_equal_n_success(self):
        assert is_multiple(5, 5)

    def test_4_multiple_by_2_is_equal_8_success(self):
        assert is_multiple(n=8, m=4)

    def test_5_multiple_by_3_is_equal_15_success(self):
        assert is_multiple(n=15, m=5)

    def test_7_is_not_multiple_by_3_failure(self):
        assert not is_multiple(n=7, m=3)


# R-1.2
class TestIsEvenFunction:
    @pytest.mark.parametrize("is_even_function", [
        is_even_version_1,
        is_even_version_2
    ])
    def test_2_is_even_success(self, is_even_function):
        assert is_even_function(2)

    @pytest.mark.parametrize("is_even_function", [
        is_even_version_1,
        is_even_version_2
    ])
    def test_10_is_even_success(self, is_even_function):
        assert is_even_function(10)

    @pytest.mark.parametrize("is_even_function", [
        is_even_version_1,
        is_even_version_2
    ])
    def test_1_is_even_failure(self, is_even_function):
        assert not is_even_function(11)


# R-1.3
class TestFindMinMaxFunction:
    @pytest.mark.parametrize("data,expected_result", [
        ([4], (4, 4)),
        ([1, 2], (1, 2)),
        ([3, 2], (2, 3)),
    ])
    def test_find_minimum_and_maximum_success(self, data, expected_result):
        assert find_min_max(data) == expected_result

    def test_find_minimum_and_maximum_failure(self):
        with pytest.raises(ValueError):
            find_min_max([])


# R-1.4 and R-1.5
class TestSumOfSquaresOfElementsToLimitFunction:
    @pytest.mark.parametrize("limit,expected_result", [
        (1, 0),
        (2, 1),
        (3, 5),
        (4, 14)
    ])
    def test_sum_of_squares_of_elements_to_limit_success(self, limit, expected_result):
        assert sum_of_squares_of_elements_to_limit(limit) == expected_result

    @pytest.mark.parametrize("limit,expected_result", [
        (1, 0),
        (2, 1),
        (3, 5),
        (4, 14)
    ])
    def test_sum_of_squares_of_elements_to_limit_comprehension_success(self, limit, expected_result):
        assert sum_of_squares_of_elements_to_limit_comprehension(limit) == expected_result


# R-1.6 and R-1.7
class TestSumOfSquaresOfElementsToLimitFunction:
    @pytest.mark.parametrize("limit,expected_result", [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 10),
        (5, 10),
    ])
    def test_sum_of_squares_of_odds_success(self, limit, expected_result):
        assert sum_of_squares_of_odds(limit=limit) == expected_result

    @pytest.mark.parametrize("limit,expected_result", [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 10),
        (5, 10),
    ])
    def test_sum_of_squares_of_odds_with_comprehension_success(self, limit, expected_result):
        assert sum_of_squares_of_odds_with_comprehension(limit=limit) == expected_result


# R-1.8
class TestMinusIndex:
    def test_minus_index_in_empty_string_success(self):
        with pytest.raises(IndexError):
            assert ''[0]

    def test_minus_index_in_one_char_string_success(self):
        assert 'a'[0]

    def test_minus_index_in_two_chars_string_success(self):
        assert 'ab'[-1] == 'ab'[1]

    def test_minus_index_in_three_chars_string_success(self):
        string = 'abc'
        assert string[-2] == string[len(string) - abs(-2)]

    def test_minus_index_in_five_chars_string_success(self):
        string = 'abcde'
        assert string[-4] == string[calculate_positive_index_from_negative(-4, len(string))]


# R-1.9 and R-1.10
class TestRanges:
    def test_positive_success(self):
        assert list(range(50, 90, 10)) == [50, 60, 70, 80]

    def test_negative_success(self):
        assert list(range(8, -10, -2)) == [8, 6, 4, 2, 0, -2, -4, -6, -8]


# R-1.11
class TestComprehension:
    def test_comprehension_success(self):
        assert [pow(2, number) for number in range(0, 9)] == [1, 2, 4, 8, 16, 32, 64, 128, 256]


# R-1.12
class TestChoiceFunction:
    def test_choice_empty_list_failure(self):
        with pytest.raises(ValueError):
            choice([], 0, 0)

    def test_choice_wrong_range_failure(self):
        with pytest.raises(ValueError):
            choice([1, 2, 3], 5, 5)

    def test_choice_for_one_element_failure(self):
        for counter in range(10):
            result = choice([1, 2, 3, 4, 5, 6, 7, 8], 2, 3)
            assert result == 3

    def test_choice_for_two_elements_failure(self):
        for counter in range(10):
            result = choice([1, 2, 3, 4, 5, 6, 7, 8], 3, 5)
            assert result in [4, 5]


# C-1.13
class TestReverseListFunction:
    def test_empty_list_success(self):
        assert reverse_list([]) == []

    def test_one_element_list_success(self):
        assert reverse_list([2]) == [2]

    def test_two_element_list_success(self):
        assert reverse_list([2, 3]) == [3, 2]

    def test_many_element_list_success(self):
        assert reverse_list([1, 2, 3, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1]


# C-1.14
class TestIsProductOddFunction:
    def test_empty_list_success(self):
        assert not is_product_odd([])

    def test_list_with_one_element_success(self):
        assert not is_product_odd([1])

    def test_list_with_two_element_where_product_is_not_odd_success(self):
        assert not is_product_odd([1, 2])

    def test_list_with_two_element_where_product_is_odd_success(self):
        assert is_product_odd([1, 3])


# C-1.15
class TestIsDistinctFunction:
    @pytest.mark.parametrize("data,expected_result", [
        ([], True),
        ([2], True),
        ([1, 2], True),
        ([4, 6, 7], True),
        ([4, 4], False),
        ([4, 3, 4], False),
        ([1, 3, 4, 4], False)
    ])
    def test_is_distinct_success(self, data, expected_result):
        assert is_distinct(data) == expected_result


# C-1.17
class TestDummyScaleFunction:
    def test_wrong_behaviour_success(self):
        assert dummy_scale([1, 2], 5) == [1, 2]


# C-1.18
class TestC1Task18:
    def test_check_result_success(self):
        elements = [0]
        [elements.append(elements[i - 1] + 2 * i) for i in range(1, 10)]
        assert elements == [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]


# C-1.19
class TestC1Task19:
    def test_check_result_success(self):
        assert [chr(i) for i in range(97, 123)] == [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]


# C-1.20
class TestMyShuffleFunction:
    def test_shuffle_success_success(self):
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        actual_result = my_shuffle(test_data)
        assert not actual_result == test_data


# C-1.22
class TestCalculateProductFunction:
    @pytest.mark.parametrize("data1,data2,expected_result", [
        ([], [], []),
        ([1], [2], [2]),
        ([1, 2], [1, 2], [1, 4]),
        ([3, 4, 5], [1, 1, 1], [3, 4, 5])
    ])
    def test_calculate_production_success(self, data1, data2, expected_result):
        assert calculate_product(data1, data2) == expected_result

    def test_data1_and_data2_have_different_size_failure(self):
        with pytest.raises(ValueError):
            assert calculate_product([1], [])


# C-1.24
class TestCountVowelsFunction:
    @pytest.mark.parametrize('word,expected_result', [
        ('', 0),
        ('a', 1),
        ('A', 1),
        ('bb', 0),
        ('abcd', 1),
    ])
    def test_count_vowels_success(self, word, expected_result):
        assert count_vowels(word) == expected_result


# C - 1.24
class TestNormFunction:
    @pytest.mark.parametrize('vector,p,expected_result', [
        ([], 1, 0),
        ([2], 2, 2),
        ([4, 3], 2, 5),
    ])
    def test_norm_success(self, vector, p, expected_result):
        assert norm(vector, p) == expected_result


# P-1.29
class TestPermutationFunction:
    def test_permutation_success(selfs):
        test_data = ['c', 'a', 't', 'd', 'o', 'g']

        assert len(permutation(test_data)) == len(list(itertools.permutations(test_data[:])))


# P-1.30
class TestHowManyTimesDeviceBy2Function:
    @pytest.mark.parametrize('number,expected_result', [
        ( 3, 1),
        (4, 2),
        (5, 2),
        (6, 2),
        (11, 3),
    ])
    def test_devide_by_success(self, number, expected_result):
        assert how_many_time_devide_by_2(number) == expected_result


# P-1.31
class TestChangeFunction:
    @pytest.mark.parametrize('charged_amount,given_amount,expected_result', [
        (1, 2, [1]),
        (2, 4, [2]),
        (10, 22, [10, 2]),
        (6, 6, []),
        (30, 44, [10, 2, 2]),
        (70, 75, [5]),
        (201, 202, [1]),
        (201, 402, [100, 100, 1]),
    ])
    def test_change_success(self, charged_amount, given_amount, expected_result):
        assert change(charged_amount=charged_amount, given_amount=given_amount) == expected_result

    def test_change_if_difference_is_lower_than_0_failure(self):
        assert change(charged_amount=100, given_amount=99) == []


# P-1.35
class TestRunBirthdayParadoxFunction:
    def test_run_birthday_paradox(self):
        how_many_case_paradox_is_fulfilled = 0
        for i in range(100):
            result = run_birthday_paradox(23)
            for key, value in result.items():
                if value >= 2:
                    how_many_case_paradox_is_fulfilled += 1

        # print(how_many_case_paradox_is_fulfilled / 100.0)

