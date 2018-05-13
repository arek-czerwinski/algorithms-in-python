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

    def __init__(self, capacity=1):
        """Create an empty array."""
        self._n = 0  # count actual elements
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
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

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


def shuffle_list(l: list):
    size = len(l)
    if size > 0:
        for index in range(size):
            changed_index = randrange(start=0, stop=size)
            reference_to_element = l[changed_index]
            l[changed_index] = l[index]
            l[index] = reference_to_element
    return l
