import pytest

from chapter_2.exercises import *


# R-2.4
class TestFlower:
    flower_name = 'arkadiusz'
    number_of_petals = 100
    price = 2.7

    FLOWER = Flower(
        name=flower_name,
        number_of_petals=number_of_petals,
        price=price
    )

    def test_constructor(self):
        flower = Flower(
            name=TestFlower.flower_name,
            number_of_petals=TestFlower.number_of_petals,
            price=TestFlower.price
        )
        assert flower._price == TestFlower.price
        assert flower._name == TestFlower.flower_name
        assert flower._number_of_petals == TestFlower.number_of_petals

    def test_get_name(self):
        assert TestFlower.FLOWER.get_name() == TestFlower.flower_name

    def test_get_price(self):
        assert TestFlower.FLOWER.get_price() == TestFlower.price

    def test_get_number_of_petals(self):
        assert TestFlower.FLOWER.get_number_of_petals() == TestFlower.number_of_petals

    def test_set_name(self):
        flower = Flower('a', 5, 25.0)
        flower.set_name('b')
        assert flower.get_name() == 'b'

    def test_set_price(self):
        flower = Flower('a', 5, 25.0)
        flower.set_price(10.0)
        assert flower.get_price() == 10.0

    def test_set_number_of_petals(self):
        flower = Flower('a', 5, 25.0)
        flower.set_number_of_petals(1)
        assert flower.get_number_of_petals() == 1


# R-2.9
class TestVector:
    def test_sub(self):
        vector1 = Vector(1)
        vector1.coords[0] = 10
        vector2 = Vector(1)
        vector2.coords[0] = 9
        vector3 = vector1 - vector2
        assert vector3.coords == [1]

    def test_neg(self):
        vector1 = Vector(1)
        vector1.coords[0] = 10
        assert (-vector1).coords == [-10]

    def test_add(self):
        vector1 = Vector(1)
        vector1.coords[0] = 10

        result = [-1] + vector1
        assert result.coords == [9]

    def test_mul(self):
        vector1 = Vector(1)
        vector1.coords[0] = 10

        result = vector1 * 2
        assert result.coords == [20]

    def test_dot_product(self):
        vector1 = Vector(1)
        vector1.coords[0] = 10
        vector2 = Vector(1)
        vector2.coords[0] = 9

        result = vector1 * vector2
        assert result == Vector(numbers=[90])


class TestReverseSequenceIterator:
    @pytest.mark.parametrize('input_sequence, expected_result', [
        ([], []),
        ([2], [2]),
        ([1, 2, 3], [3, 2, 1]),
    ])
    def test_reverse_iteration(self, input_sequence, expected_result):
        assert list(ReverseSequenceIterator(input_sequence)) == expected_result


class TestRange:
    # C-2.27
    @pytest.mark.parametrize('input_sequence, range_obj, expected_result', [
        (0, Range(0), True),
        (1, Range(1), False),
        (1, Range(0, 2), True),
        (1, Range(0, 2, 2), True),
    ])
    def test__contains__(self, input_sequence, range_obj, expected_result):
        pass
