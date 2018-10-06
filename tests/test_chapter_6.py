import pytest

from chapter_6.exercises import remove_all_elements_from_stack, transfer_from_stack_to_stack, reverse, \
    ArithmeticExpressionCalculator


class TestTransferFromStackToStackFunction:
    @pytest.mark.parametrize(
        'stack_a, stack_b, expected_result', [
            ([], [], []),
            [[1], [], [1]],
            [[1, 2], [], [2, 1]],
            [[1, 2, 3], [], [3, 2, 1]],
            [[3, 2, 1], ['A', 'B'], ['A', 'B', 1, 2, 3]],
        ]
    )
    def test_transfer_from_stack_to_stack(self, stack_a, stack_b, expected_result):
        transfer_from_stack_to_stack(stack_a=stack_a, stack_b=stack_b)
        assert stack_b == expected_result


class TestRemoveAllElementsFromStackFunction:
    @pytest.mark.parametrize(
        'stack, expected_result', [
            ([], []),
            [[1], []],
            [[1, 2], []],
            [[1, 2, 3], []],
            [[-2, -1, 0, 1, 2, 3], []],
        ]
    )
    def test_remove_all_elements_from_stack(self, stack, expected_result):
        actual_result = remove_all_elements_from_stack(stack=stack)
        assert actual_result == expected_result


class TestReverseFunction:
    @pytest.mark.parametrize(
        'elements, expected_result', [
            ([], []),
            [[1], [1]],
            [[1, 2], [2, 1]],
            [[1, 2, 3], [3, 2, 1]],
            [[-2, -1, 0, 1, 2, 3], [3, 2, 1, 0, -1, -2]],
        ]
    )
    def test_reverse(self, elements, expected_result):
        actual_result = reverse(elements=elements)
        assert actual_result == expected_result


class TestArithmeticExpressionCalculator:
    @pytest.mark.parametrize(
        'expression, expected_result', [
            ('1 + 1', {'_expression': '1 + 1', '_parsed_expression': ['1', '+', '1']})
        ]
    )
    def test___init__(self, expression, expected_result):
        assert vars(ArithmeticExpressionCalculator(expression=expression)) == expected_result

    @pytest.mark.parametrize(
        'expression, expected_result', [
            ('', []),
            (' ', []),
            ('1', ['1']),
            ('1 ', ['1']),
            ('1 +', ['1', '+']),
            (' 1 + ', ['1', '+']),
            ('1   + 1', ['1', '+', '1']),
        ]
    )
    def test__split_expression(self, expression, expected_result):
        actual_result = ArithmeticExpressionCalculator._split_expression(
            expression=expression
        )
        assert actual_result == expected_result

    def test_something(self):
        class Expression:
            def __init__(self, splited_expression: list) -> None:
                self._splited_expression = splited_expression
                self._operators = {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y
                }

            def calculate(self):
                if len(self._splited_expression) == 1:
                    return int(self._splited_expression[0])

                if self._splited_expression[0] == '(':
                    index_right_parenthais = self._splited_expression.index(object=')')
                    if self._splited_expression[index_right_parenthais] != ')':
                        raise ValueError(
                            f'wrong parenthesis {self._splited_expression[0]} '
                            f'and {self._splited_expression[-1]}'
                        )
                    new_expression = Expression(splited_expression=self._splited_expression[1:-1])
                    return new_expression.calculate()
                else:
                    operator = self._operators[self._splited_expression[1]]
                    result = operator(
                        Expression(splited_expression=self._splited_expression[:1]).calculate(),
                        Expression(splited_expression=self._splited_expression[2:]).calculate(),
                    )
                    return result




        # result = Expression(splited_expression=['1', '+', '1', '-', '1', '-', '1']).calculate()
        result = Expression(splited_expression=['(', '1', '+', '1', ')', '-', '(' '1', '-', '1', ')']).calculate()
        print('==============> ', result)
