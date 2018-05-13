import random
from random import randrange, randint


# R-1.1
def is_multiple(n: int, m: int):
    if m > n:
        return False
    else:
        for i in range(1, n):
            if m * i == n:
                return True

        return False


# R-1.2
def is_even_version_1(number: int):
    result = divmod(number, 2)
    if not result[1]:
        return True
    else:
        return False


# R-1.2
def is_even_version_2(number: int):
    return not number & 1


# R-1.3
def find_min_max(data):
    if not len(data):
        raise ValueError('data is empty')
    minimum = data[0]
    maximum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element

    return minimum, maximum


# R-1.4
def sum_of_squares_of_elements_to_limit(limit: int):
    sum_all_elements = 0
    for number in range(1, limit):
        sum_all_elements += number * number

    return sum_all_elements


# R-1.5
def sum_of_squares_of_elements_to_limit_comprehension(limit: int):
    return sum([pow(number, 2) for number in range(1, limit)])


# R-1.6
def sum_of_squares_of_odds(limit: int):
    sum_of_elements = 0
    for number in range(1, limit):
        if not is_even_version_2(number=number):
            sum_of_elements += pow(number, 2)

    return sum_of_elements


# R-1.7
def sum_of_squares_of_odds_with_comprehension(limit: int):
    return sum([pow(number, 2) for number in range(1, limit) if not is_even_version_2(number=number)])


# R-1.8
def calculate_positive_index_from_negative(negative_index: int, size: int):
    return size - abs(negative_index)


# R-1.12
def choice(data: list, start: int, end: int):
    if not len(data):
        raise ValueError('data is empty')
    if end - start < 1:
        raise ValueError('range is lower than 1')
    return data[randrange(start=start, stop=end)]


# C-1.13
def reverse_list(data: list):
    if len(data) <= 1:
        return data
    result = []
    for reverse_index in range((len(data) - 1), -1, -1):
        result.append(data[reverse_index])

    return result


# C-1.14
def is_product_odd(data: list):
    for i in data:
        for j in data:
            if i != j and (i * j) & 1 == 1:
                return True
    return False


# C-1.15
def is_distinct(data: list):
    size = len(data)
    for index_of_current_number in range(size):
        for index_of_next_number in range(index_of_current_number + 1, size):
            if data[index_of_current_number] == data[index_of_next_number]:
                return False

    return True


# def scale(data, factor):
#     for j in range(len(data):
#     data[j] = factor


# C-1.16
# Numbers in python are immutable but list is mutable to it possible in iteration to change values in list.

# C-1.17
# Because assign new value to variable and not to list
def dummy_scale(data, factor):
    for val in data:
        val = factor
    return data


def my_shuffle(data: list):
    result = []
    tmp_data = list(data)
    for i in range(len(data)):
        if len(tmp_data) > 0:
            index = randint(0, len(tmp_data) - 1)
            element = tmp_data[index]
            del tmp_data[index]

            result.append(element)

    return result


# C-1.22
def calculate_product(data1: list, data2: list):
    if len(data1) != len(data2):
        raise ValueError('input data have different size')

    return [data1[index] * data2[index] for index in range(len(data1))]


VOWELS = ['a', 'e', 'i', 'o', 'u']


# C - 1.24
def count_vowels(word: str):
    word_lower_case = word.lower()
    return sum([1 for letter in word_lower_case if letter in VOWELS])


def norm(v: list, p: int = 2):
    total_sum = sum([pow(number, 2) for number in v])
    return pow(total_sum, 1 / p)


def permutation(elements: list):
    if len(elements) == 0:
        return []
    elif len(elements) == 1:
        return [elements]
    else:
        result = []
        for index in range(len(elements)):
            letter = elements[index]
            rest_letters = elements[:index] + elements[index + 1:]
            for part in permutation(rest_letters):
                result.append([letter] + part)

    return result


def how_many_time_devide_by_2(number: int):
    if number <= 2:
        raise ValueError('value should be more than 2')

    counter = 0
    float_number = 1.0 * number
    while float_number >= 2.0:
        float_number /= 2.0
        counter += 1

    return counter


MONETARY_SYSTEM = [100, 50, 20, 10, 5, 2, 1]


# P-1.31
def change(charged_amount: int, given_amount: int):
    print()
    result = []
    difference = given_amount - charged_amount
    if difference <= 0:
        return result
    amount = 0
    monetary_index = 0
    while amount <= difference and monetary_index < len(MONETARY_SYSTEM):
        if amount + MONETARY_SYSTEM[monetary_index] <= difference:
            amount += MONETARY_SYSTEM[monetary_index]
            result.append(MONETARY_SYSTEM[monetary_index])
        else:
            monetary_index += 1

    return result


def run_birthday_paradox(how_many_people: int):
    birthdays = dict()
    for i in range(how_many_people):
        birthday = random.randint(0, 365)
        birthdays[birthday] = birthdays.get(birthday, 0) + 1

    return birthdays
