from collections import defaultdict
from random import randrange


# R-5.1
def fragment_code1(n: int):
    import sys
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        data.append(1)
        print("Length: {0: 3d};Size in bytes: {1: 4d} ".format(a, b))


# R-5.2
def fragment_code1_when_list_is_exceeded(n: int):
    import sys
    data = []
    previous = 0
    for k in range(n):
        a = len(data)
        data.append(1)
        b = sys.getsizeof(data)
        if b != previous:
            print("Length: {0: 3d};Size in bytes: {1: 4d} ".format(a, b))
            previous = b


# R-5.3
def framegment_code1_when_list_is_shrink(n):
    data = []
    for k in range(n):
        data.append(1)

    import sys
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        data.pop()
        print("Length: {0: 3d};Size in bytes: {1: 4d} ".format(a, b))


# source code from chapter 5
class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self, capacity=1, capacity_factor=2):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity_factor = capacity_factor
        self._capacity = capacity  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    # R-5.4 Our DynamicArray class, as given in Code Fragment 5.3, does not support
    # use of negative indices with getitem . Update that method to better
    # match the semantics of a Python list.
    def __getitem__(self, k):
        """Return element at index k."""

        if 0 <= k < self._n:
            return self._A[k]
        if k < 0 and abs(k) <= self._n:
            return self._A[k + self._n]

        raise IndexError('wrong index')

    def append(self, obj):
        if obj is None:
            return
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(self._capacity_factor * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, new_capacity):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(new_capacity)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use new array
        self._capacity = new_capacity

    @staticmethod
    def _make_array(c):  # nonpublic utitity
        """Return new array with capacity c."""
        return [None] * c  # (c * ctypes.py_object)()  # see ctypes documentation

    @staticmethod
    def _move_elements(from_array, to_array, from_index, to_index, start_index):
        for index in range(from_index, to_index):
            to_array[start_index] = from_array[index]
            start_index += 1

        return to_array

    def insert(self, index, value):
        """Insert value at index k, shifting subsequent values rightward."""
        if value is None:
            return
        if self._n == self._capacity:
            new_array = self._make_array(2 * self._capacity)
            new_array = self._move_elements(  # move element from the beginning to index -1
                from_array=self._A,
                to_array=new_array,
                from_index=0,
                to_index=index,
                start_index=0
            )
            new_array = self._move_elements(
                from_array=self._A,
                to_array=new_array,
                from_index=index,
                to_index=self._n,
                start_index=index + 1
            )
            self._capacity = 2 * self._capacity
            self._A = new_array
        self._A[index] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item
                return  # exit immediately
        raise ValueError('value not found')  # only reached if no match

    # C-5.16 Implement a pop method for the DynamicArray class, given in Code Frag-
    # ment 5.3, that removes the last element of the array, and that shrinks the
    # capacity, N, of the array by half any time the number of elements in the
    # array goes below N/4.
    def pop(self):
        if self._n == 0:
            raise ValueError('Can not pop element on empty array')

        last_element = self._remove_last_element()

        if self._is_shrinkable_array():
                self._resize(
                    new_capacity=self._calculate_shrinked_array_size(
                        capacity=self._capacity,
                        capacity_factor=self._capacity_factor
                    )
                )

        return last_element

    def _is_shrinkable_array(self):
        return 1 <= self._n == self._calculate_shrinked_array_size(
            capacity=self._capacity,
            capacity_factor=self._capacity_factor
        )

    @staticmethod
    def _calculate_shrinked_array_size(capacity, capacity_factor):
        return int(capacity / capacity_factor)

    def _remove_last_element(self):
        last_element = self._A[self._n - 1]

        self._A[self._n - 1] = None
        self._n = self._n - 1

        return last_element


# R-5.7 Let A be an array of size n ≥ 2 containing integers from 1 to n − 1, inclu-
# sive, with exactly one repeated. Describe a fast algorithm for finding the
# integer in A that is repeated.
def find_repeated_number(numbers: list):
    length = len(numbers)
    counter = [0] * length
    for number in numbers:
        counter[number - 1] = counter[number - 1] + 1
        if counter[number - 1] > 1:
            return number

    raise ValueError('not found repeated number!')


# R-5.9 Explain the changes that would have to be made to the program of Code
# Fragment 5.11 so that it could perform the Caesar cipher for messages
# that are written in an alphabet-based language other than English, such as
# Greek, Russian, or Hebrew.

# R-5.10 is implemented. Instead of list use string. The logic is the same
# R-5.10 The constructor for the CaesarCipher class in Code Fragment 5.11 can
# be implemented with a two-line body by building the forward and back-
# ward strings using a combination of the join method and an appropriate
# comprehension syntax. Give such an implementation.
class GeneralCaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, alphabet: str, shift=1):
        """Construct Caesar cipher using given integer shift for rotation."""
        self._alphabet = list(alphabet)
        self._shift = shift % len(self._alphabet)
        self._shifted_alphabet = \
            self._alphabet[self._shift:len(self._alphabet)] + self._alphabet[0:self._shift]

    def encrypt(self, message):
        return self._transform(
            message=message,
            source_alphabet=self._alphabet,
            shifter_alphabet=self._shifted_alphabet
        )

    def _transform(self, message, source_alphabet, shifter_alphabet):
        result = list()
        # TODO: this should be improved: dictionary
        for chr in message:
            for i in range(len(source_alphabet)):
                if source_alphabet[i] == chr:
                    result.append(shifter_alphabet[i])
                    break
        return ''.join(result)

    def decrypt(self, message):
        return self._transform(
            message=message,
            source_alphabet=self._shifted_alphabet,
            shifter_alphabet=self._alphabet
        )


# R-5.11 Use standard control structures to compute the sum of all numbers in an
# n × n data set, represented as a list of lists.
def sum_matrix(matrix_2d):
    result = 0.0
    for i in range(len(matrix_2d)):
        for j in range(len(matrix_2d[0])):
            result += matrix_2d[i][j]
    return result


# R-5.12 Describe how the built-in sum function can be combined with Python’s
# comprehension syntax to compute the sum of all numbers in an n × n data
# set, represented as a list of lists.
def sum_matrix_with_comprehension(matrix_2d):\
    return sum([number for numbers in matrix_2d for number in numbers])


# C-5.14 The shuffle method, supported by the random module, takes a Python
# list and rearranges it so that every possible ordering is equally likely.
# Implement your own version of such a function. You may rely on the
# randrange(n) function of the random module, which returns a random
# number between 0 and n − 1 inclusive.
def shuffle_list(elements: list):
    size = len(elements)
    if size > 0:
        for index in range(size):
            changed_index = randrange(start=0, stop=size)
            reference_to_element = elements[changed_index]
            elements[changed_index] = elements[index]
            elements[index] = reference_to_element
    return elements


# C-5.15 Consider an implementation of a dynamic array, but instead of copying
# the elements into an array of double the size (that is, from N to 2N) when
# its capacity is reached, we copy the elements into an array with N/4
# additional cells, going from capacity N to capacity N + N/4. Prove that
# performing a sequence of n append operations still runs in O(n) time in
# this case
# Answer - amortization of adding or remove elements in array

# C-5.17 Prove that when using a dynamic array that grows and shrinks as in the
# previous exercise, the following series of 2n operations takes O(n) time:
# n append operations on an initially empty array, followed by n pop oper-
# ations.
# very good explanation http://www.cse.cuhk.edu.hk/~taoyf/course/comp3506/lec/dyn-array.pdf

#  assumptions
#  n insert operation takes n which was proven by n inserts operations
#  divided by number insertions taken previously which is
#  n / 2.  (c * n) / (n / 2) = 2c => c (adding one element to array)

#  prove of popping takes n time. limit to shrink the array is n/4 so it is needed to take 3/4n pop operations.
#  Input array size is n so (c*3/4n)/ n = 3/4c => c cost of one operation

#  C-5.18 the same as above
#  C-5.19 the same as above


# C-5.25 The syntax data.remove(value) for Python list data removes only the first
# occurrence of element value from the list. Give an implementation of a
# function, with signature remove all(data, value), that removes all occur-
# rences of value from the given list, such that the worst-case running time
# of the function is O(n) on a list with n elements. Not that it is not efficient
# enough in general to rely on repeated calls to remove.
def remove_all(elements: list, element_to_remove):
    result = list()
    for element in elements:
        if element != element_to_remove:
            result.append(element)

    return result


# C-5.26 Let B be an array of size n ≥ 6 containing integers from 1 to n − 5, inclu-
# sive, with exactly five repeated. Describe a good algorithm for finding the
# five integers in B that are repeated.
def find_repeated_numbers(numbers: list, repetition_number):
    number_occurrence = defaultdict(list)
    for number in numbers:
        occurrence = number_occurrence[number]
        occurrence.append(number)
        if len(occurrence) == repetition_number:
            return number

    return None
