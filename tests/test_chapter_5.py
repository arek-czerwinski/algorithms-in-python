import datetime
import pytest

from chapter_5.exercises import (
    fragment_code1,
    fragment_code1_when_list_is_exceeded,
    framegment_code1_when_list_is_shrink,
    DynamicArray,
    find_repeated_number,
    GeneralCaesarCipher,
    sum_matrix, sum_matrix_with_comprehension, shuffle_list, remove_all, find_repeated_numbers)
from tests.utils import create_dynamic_array_with_specific_number_of_elements, create_dynamic_array_with_added_elements


class TestFragmentCode:
    @pytest.mark.parametrize(
        'n', [
            256
        ]
    )
    # R-5.1
    def test_fragment_code1(self, n):
        fragment_code1(n=n)

    @pytest.mark.parametrize(
        'n', [
            256
        ]
    )
    # R-5.2
    def test_fragment_code1_when_list_is_exceeded(self, n):
        fragment_code1_when_list_is_exceeded(n=n)

    @pytest.mark.parametrize(
        'n', [
            256
        ]
    )
    # R-5.3
    def test_framegment_code1_when_list_is_shrink(self, n):
        framegment_code1_when_list_is_shrink(n=n)


class TestDynamicArray:
    # R-5.4
    @pytest.mark.parametrize(
        'how_many_elements_to_add, index, expected_result', [
            (3, 0, 0),
            (3, 1, 1),
            (3, 2, 2),
            (3, -1, 2),
            (3, -2, 1),
            (3, -3, 0),
            (1, -1, 0),
            (2, 0, 0),
            (2, 1, 1),
            (2, -1, 1),
            (2, -2, 0),
            (1, -1, 0),
            (1, 0, 0),
        ]
    )
    def test___getitem__(self, how_many_elements_to_add, index, expected_result):
        array = create_dynamic_array_with_specific_number_of_elements(
            how_many_elements_to_add=how_many_elements_to_add
        )
        actual_result = array[index]
        assert actual_result == expected_result

    # R-5.4
    @pytest.mark.parametrize(
        'how_many_elements_to_add, index', [
            (1, 1),
            (2, 2),
            (2, -3),
        ]
    )
    def test___getitem__negtive_scenarios(self, how_many_elements_to_add, index):
        array = create_dynamic_array_with_specific_number_of_elements(
            how_many_elements_to_add=how_many_elements_to_add
        )

        with pytest.raises(IndexError) as error:
            array[index]

    # R-5.4
    @pytest.mark.parametrize(
        'how_many_elements_to_add, index, number, expected_result', [
            (1, 0, 100, [100, 0]),
            (2, 0, 100, [100, 0, 1, None]),
            (2, 1, 100, [0, 100, 1, None]),
            (4, 0, 100, [100, 0, 1, 2, 3, None, None, None]),
            (4, 1, 100, [0, 100, 1, 2, 3, None, None, None]),
            (4, 2, 100, [0, 1, 100, 2, 3, None, None, None]),
            (4, 3, 100, [0, 1, 2, 100, 3, None, None, None]),
            (4, 4, 100, [0, 1, 2, 3, 100, None, None, None]),
        ]
    )
    def test_insert(self, how_many_elements_to_add, index, number, expected_result):
        array = create_dynamic_array_with_specific_number_of_elements(
            how_many_elements_to_add=how_many_elements_to_add
        )
        array.insert(index=index, value=number)
        assert array._A == expected_result

    @pytest.mark.parametrize(
        'from_array, to_array, from_index, to_index, start_index, expected_result', [
            ([], [], 0, 0, 0, []),
            ([1], [None], 0, 0, 0, [None]),
            ([1], [None], 0, 1, 0, [1]),
            ([1, 2, 3, 4, 5], [None] * 5, 0, 1, 0, [1, None, None, None, None]),
            ([1, 2, 3, 4, 5], [None] * 5, 0, 2, 0, [1, 2, None, None, None]),
            ([1, 2, 3, 4, 5], [None] * 5, 0, 3, 0, [1, 2, 3, None, None]),
            ([1, 2, 3, 4, 5], [None] * 5, 1, 2, 0, [2, None, None, None, None]),
            ([1, 2, 3, 4, 5], [None] * 5, 1, 2, 1, [None, 2, None, None, None]),
            ([1, 2, 3, 4, 5], [None] * 5, 1, 3, 2, [None, None, 2, 3, None]),
        ]
    )
    def test__move_elements(self, from_array, to_array, from_index, to_index, start_index, expected_result):
        array = DynamicArray()
        actual_result = array._move_elements(
            from_array=from_array,
            to_array=to_array,
            from_index=from_index,
            to_index=to_index,
            start_index=start_index
        )
        assert actual_result == expected_result

    # C-5.16 Implement a pop method for the DynamicArray class, given in Code Frag-
    # ment 5.3, that removes the last element of the array, and that shrinks the
    # capacity, N, of the array by half any time the number of elements in the
    # array equelas N/2.
    @pytest.mark.parametrize(
        'elements_to_add, expected_popped_element, expected_array', [
            (range(0,8), 7, [0, 1, 2, 3, 4, 5, 6, None]),
            ([0, 1, 2, 3, 4, 5, 6, None], 6, [0, 1, 2, 3, 4, 5, None, None]),
            ([0, 1, 2, 3, 4, None, None, None], 4, [0, 1, 2, 3]),
            ([0, 1, 2, 3, 4, 5, None, None], 5, [0, 1, 2, 3, 4, None, None, None]),
            ([0, 1, 2, 3], 3, [0, 1, 2, None]),
            ([0, 1, 2, None], 2, [0, 1]),
            ([0, 1], 1, [0]),
            ([0], 0, [None]),
        ]
    )
    def test_pop(self, elements_to_add, expected_popped_element, expected_array):
        array = create_dynamic_array_with_added_elements(elements_to_add)
        popped_element = array.pop()
        assert popped_element == expected_popped_element
        assert array._A == expected_array

    @pytest.mark.parametrize(
        'dynamic_array', [
            DynamicArray()
        ]
    )
    def test_pop_negative_scenario(self, dynamic_array):
        with pytest.raises(ValueError):
            dynamic_array.pop()


# R-5.7
class TestFindRepeatedNumberFunction:
    @pytest.mark.parametrize(
        'numbers, expected_result', [
            ([1, 1], 1),
            ([1, 2, 1], 1),
            ([2, 1, 1], 1),
            ([2, 1, 2], 2),
            ([1, 2, 3, 3], 3)
        ]
    )
    def test_find_repeated_function(self, numbers, expected_result):
        actual_result = find_repeated_number(numbers=numbers)
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'numbers', [
            ([1, 2])
        ]
    )
    def test_find_repeated_number__negative_scenario(self, numbers):
        with pytest.raises(ValueError):
            find_repeated_number(numbers=numbers)


# R-5.8 Experimentally evaluate the efficiency of the pop method of Python’s list
# class when using varying indices as a parameter, as we did for insert on
# page 205. Report your results akin to Table 5.5.
class TestPopMethodInList:
    @pytest.mark.parametrize(
        'how_many_elements, index_of_element_to_pop', [
            (10, 0),
            (10, 5),
            (10, 9),
            (100, 0),
            (100, 50),
            (100, 99),
            (1000, 0),
            (1000, 500),
            (1000, 999),
            (10000, 0),
            (10000, 5000),
            (10000, 9999),
            (100000, 0),
            (100000, 50000),
            (100000, 99999),
        ]
    )
    def test_pop_method_in_list(self, how_many_elements, index_of_element_to_pop):
        list_with_elements = list(range(how_many_elements))
        start_time = datetime.datetime.now()
        list_with_elements.pop(index_of_element_to_pop)
        end_time = datetime.datetime.now()

        print(
            'for  ',
            how_many_elements,
            'in list tried get element ',
            index_of_element_to_pop,
            'in time',
            end_time - start_time
        )


ENGLISH_ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVXYZ'


class TestCaesarCipher:
    @pytest.mark.parametrize(
        ' alphabet, shift, expected_result', [
            ('abcdefg', 2, list('cdefgab')),
            ('abcdefg', 1, list('bcdefga')),
            ('abcdefg', 0, list('abcdefg')),
            ('abcdefg', 7, list('abcdefg')),
            ('abcdefg', 8, list('bcdefga'))
        ]
    )
    def test_constructor(self, alphabet: str, shift, expected_result):
        cipher = GeneralCaesarCipher(alphabet=alphabet, shift=shift)
        assert cipher._shifted_alphabet == expected_result

    @pytest.mark.parametrize(
        ' alphabet, shift, message, expected_result', [
            (ENGLISH_ALPHABET, 2, 'A', 'C'),
            (ENGLISH_ALPHABET, 2, 'AZ', 'CB'),
            (ENGLISH_ALPHABET, 1, 'Z', 'A'),
            (ENGLISH_ALPHABET, 1, 'AREK', 'BSFL'),
            (ENGLISH_ALPHABET, 1, 'ZUZA', 'AVAB'),
        ]
    )
    def test_encrypt(self, alphabet: str, shift, message, expected_result):
        cipher = GeneralCaesarCipher(alphabet=alphabet, shift=shift)
        assert cipher.encrypt(message=message) == expected_result

    @pytest.mark.parametrize(
        ' alphabet, shift, message, expected_result', [
            (ENGLISH_ALPHABET, 2, 'C', 'A'),
            (ENGLISH_ALPHABET, 2, 'CB', 'AZ'),
            (ENGLISH_ALPHABET, 1, 'A', 'Z'),
            (ENGLISH_ALPHABET, 1, 'BSFL', 'AREK'),
            (ENGLISH_ALPHABET, 1, 'AVAB', 'ZUZA'),
        ]
    )
    def test_decrypt(self, alphabet: str, shift, message, expected_result):
        cipher = GeneralCaesarCipher(alphabet=alphabet, shift=shift)
        assert cipher.decrypt(message=message) == expected_result


# R-5.11
class TestSumMatrixFunction:
    @pytest.mark.parametrize(
        'matrix, expected_result', [
            ([[0]], 0.0),
            ([[1]], 1.0),
            ([[1, 1]], 2.0),
            ([[1, 1], [1, 1]], 4.0),
            ([[1, 1], [1, 1], [1, 1]], 6.0),
            ([[3, 3, 3, 3], [3, 3, 3, 3]], 24.0),
        ]
    )
    def test_sum_matrix(self, matrix, expected_result):
        assert sum_matrix(matrix_2d=matrix) == expected_result


# R-5.12
class TestSumMatrixWithComprehensionFunction:
    @pytest.mark.parametrize(
        'matrix, expected_result', [
            ([[0]], 0),
            ([[1]], 1),
            ([[1, 1]], 2),
            ([[1, 1], [1, 1]], 4),
            ([[1, 1], [1, 1], [1, 1]], 6),
            ([[3, 3, 3, 3], [3, 3, 3, 3]], 24),
        ]
    )
    def test_sum_matrix_with_comprehension(self, matrix, expected_result):
        assert sum_matrix_with_comprehension(matrix_2d=matrix) == expected_result


class TestPerformanceWithNotEmptyListInConstructor:
    @pytest.mark.parametrize(
        'capacity, how_many_elements_to_add', [
            (1, 100),
            (10, 100),
            (20, 100),
            (50, 100),
            (75, 100),
            (99, 100),
            (100, 100),
            (199, 100),
            (500, 100),
            (1000, 100),
        ]
    )
    def test_performance(self, capacity, how_many_elements_to_add):
        start_time = datetime.datetime.now()
        print('********** PERFORMANCE TEST FOR CAPACITY', capacity, ' ******')

        print('capacity for dynamic array', capacity, ', start time: ', start_time)

        create_dynamic_array_with_specific_number_of_elements(
            how_many_elements_to_add=how_many_elements_to_add,
            capacity=capacity
        )
        end_time = datetime.datetime.now()
        print('capacity for dynamic array', capacity, ', end time: ', start_time)
        print('capacity for dynamic array', capacity, ', time difference : ', end_time - start_time)
        print('********** PERFORMANCE TEST FOR CAPACITY', capacity, ' ******')


# C-5.14
class TestShuffleList:
    @pytest.mark.parametrize(
        'input_list, expected_result', [
            ([], []),
            ([2], [2])
        ]
    )
    def test_shuffle_list_for_empty_and_list_with_one_element(
            self,
            input_list,
            expected_result
    ):
        actual_result = shuffle_list(elements=input_list)
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'input_list, expected_result', [
            ([1, 2], [1, 2]),
            ([1, 2, 3], [1, 2, 3])
        ]
    )
    def test_shuffle_list_for_more_than_two_elements(
            self,
            input_list,
            expected_result
    ):
        actual_result = None
        for i in range(10):
            actual_result = shuffle_list(elements=input_list)
            if actual_result != expected_result:
                break
        assert not actual_result == expected_result


class TestRemoveAllFunction:
    @pytest.mark.parametrize(
        'elements, element_to_remove, expected_result', [
            ([], None, []),
            ([1], 0, [1]),
            ([1], 1, []),
            ([0, 1], 2, [0, 1]),
            ([0, 1], 1, [0]),
            ([1, 0, 1], 1, [0]),
            ([0, 1, 0, 2, 3, 0], 0, [1, 2, 3]),
        ]
    )
    def test_remove_all(self, elements, element_to_remove, expected_result):
        actual_result = remove_all(elements=elements, element_to_remove=element_to_remove)
        assert sorted(actual_result) == sorted(expected_result)


class TestFindRepeatedNumbersFunction:
    @pytest.mark.parametrize(
        'numbers, repetition_number, expected_result', [
            ([1], 1, 1),
            ([1], 2, None),
            ([1, 1], 2, 1),
            ([1, 3, 2, 4], 2, None),
            ([1, 3, 3, 4], 2, 3),
            ([1, 3, 1, 1, 1, 1], 5, 1),
            ([1, 3, 1, 1, 1, 1], 5, 1),
            ([1, 3, 1, 1, 2, 1], 5, None),
            ([1, 3, 2, 2, 2, 2, 1, 1, 1, 1], 5, 1),
            ([1, 3, 2, 2, 2, 2, 1, 1, 1, 3], 5, None),
        ]
    )
    def test_find_repeated_numbers(self, numbers, repetition_number, expected_result):
        actual_result = find_repeated_numbers(numbers=numbers, repetition_number=repetition_number)
        assert actual_result == expected_result
