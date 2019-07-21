import pytest

from chapter_7.exercises import MySingleNode, MySingleLinkedList, get_number_of_nodes, MyDoubleLinkedList, \
    MyDoubledLinkedNode

from utils.errors import EmptyCollection, ValueNotFoundError


class TestMySingleNode:
    @pytest.mark.parametrize(
        'next_node, value, expected_value', [
            (None, 'some_value', {'next_node': None, 'value': 'some_value'}),
            (
                    MySingleNode(None, 'another_value'), 'some_value', {
                        'next_node': MySingleNode(None, 'another_value').to_dict()
                        ,
                        'value': 'some_value',
                    }
            ),
        ]
    )
    def test__init__(self, next_node, value, expected_value):
        node = MySingleNode(next_node=next_node, value=value)
        actual_result = node.to_dict()
        assert actual_result == expected_value


class TestMySingleLinkedList:
    @pytest.mark.parametrize(
        'my_list, size, expected_result',
        [
            (MySingleLinkedList(), 0, True),
            (MySingleLinkedList(), 1, False),
        ]
    )
    def test_is_empty(self, my_list, size, expected_result):
        my_list._size = size
        actual_result = my_list.is_empty()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'values_to_add, expected_state',
        [
            (list(), {'_head': None, '_tail': None, '_size': 0}),
            (
                    [1],
                    {
                        '_head': MySingleNode(None, 1).to_dict(),
                        '_tail': MySingleNode(None, 1).to_dict(),
                        '_size': 1
                    }
            ),
            (
                    [1, 2],
                    {
                        '_head': MySingleNode(MySingleNode(None, 2), 1).to_dict(),
                        '_tail': MySingleNode(None, 2).to_dict(),
                        '_size': 2
                    }
            ),
            (
                    [1, 2, 3],
                    {
                        '_head': MySingleNode(MySingleNode(MySingleNode(None, 3), 2), 1).to_dict(),
                        '_tail': MySingleNode(None, 3).to_dict(),
                        '_size': 3

                    }
            ),
        ]
    )
    def test_add_element_at_tail(self, values_to_add, expected_state):
        instance = MySingleLinkedList()
        for value in values_to_add:
            instance.add_element_at_tail(value=value)

        actual_state = instance.to_dict()
        assert actual_state == expected_state

    @pytest.mark.parametrize(
        'instance, expected_result',
        [
            (
                    MySingleLinkedList(
                        head=None,
                        tail=None,
                        size=0
                    ),
                    list()
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1
                    ),
                    [1]
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(None, 2), 1),
                        tail=MySingleNode(None, 2),
                        size=2
                    ),
                    [1, 2]
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(MySingleNode(None, 3), 2), 1),
                        tail=MySingleNode(None, 3),
                        size=3
                    ),
                    [1, 2, 3]
            ),
        ]
    )
    def test_get_all_values(self, instance, expected_result):
        actual_result = instance.get_all_values()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'instance, expected_value, expected_state',
        [
            (
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1
                    ),
                    1,
                    MySingleLinkedList().to_dict()
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(None, 2), 1),
                        tail=MySingleNode(None, 2),
                        size=2
                    ),
                    1,
                    MySingleLinkedList(
                        head=MySingleNode(None, 2),
                        tail=MySingleNode(None, 2),
                        size=1
                    ).to_dict()
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(MySingleNode(None, 3), 2), 1),
                        tail=MySingleNode(None, 3),
                        size=3
                    ),
                    1,
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(None, 3), 2),
                        tail=MySingleNode(None, 3),
                        size=2
                    ).to_dict()
            ),
        ]
    )
    def test_get_first_and_remove(self, instance, expected_value, expected_state):
        actual_value = instance.get_first_and_remove()
        actual_state = instance.to_dict()
        assert actual_value == expected_value
        assert actual_state == expected_state

    @pytest.mark.parametrize(
        'instance',
        [
            (
                    MySingleLinkedList(
                        head=None,
                        tail=None,
                        size=0
                    )
            ),
        ]
    )
    def test_get_first_and_remove_on_empty_list(self, instance):
        with pytest.raises(EmptyCollection):
            instance.get_first_and_remove()

    SINGLE_NODE_100 = MySingleNode(None, 100)
    SINGLE_NODE_101 = MySingleNode(None, 101)
    SINGLE_NODE_104 = MySingleNode(None, 104)

    @pytest.mark.parametrize(
        'current_instance, other_instance, expected_state',
        [
            (
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1
                    ),
                    MySingleLinkedList(),
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1
                    ).to_dict()
            ),
            (
                    MySingleLinkedList(),
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1
                    ),
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1
                    ).to_dict()
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(SINGLE_NODE_100, 1),
                        tail=SINGLE_NODE_100,
                        size=2
                    ),
                    MySingleLinkedList(
                        head=MySingleNode(None, 3),
                        tail=MySingleNode(None, 3),
                        size=1
                    ),
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(MySingleNode(None, 3), 100), 1),
                        tail=MySingleNode(None, 3),
                        size=3
                    ).to_dict(),
            ),
            (
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(SINGLE_NODE_101, 2), 1),
                        tail=SINGLE_NODE_101,
                        size=3
                    ),
                    MySingleLinkedList(
                        head=MySingleNode(SINGLE_NODE_104, 2),
                        tail=SINGLE_NODE_104,
                        size=2
                    ),
                    MySingleLinkedList(
                        head=MySingleNode(
                            MySingleNode(
                                MySingleNode(
                                    MySingleNode(
                                        MySingleNode(None, 104),
                                        2
                                    ),
                                    101
                                ),
                                2
                            ),
                            1
                        ),
                        tail=MySingleNode(None, 104),
                        size=5
                    ).to_dict(),
            ),
        ]
    )
    def test_extend(self, current_instance, other_instance, expected_state):
        result = current_instance.extend(other_instance)
        actual_state = result.to_dict()
        assert actual_state == expected_state

    @pytest.mark.parametrize(
        'values_to_add, value_1_to_swap, value_2_to_swap, expected_state',
        [
            (
                    [1],
                    1,
                    1,
                    MySingleLinkedList(
                        head=MySingleNode(None, 1),
                        tail=MySingleNode(None, 1),
                        size=1,
                    ).to_dict()
            ),
            (

                    [1, 2],
                    1,
                    2,
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(None, 1), 2),
                        tail=MySingleNode(None, 1),
                        size=2,
                    ).to_dict()
            ),
            (
                    [1, 2],
                    2,
                    1,
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(None, 1), 2),
                        tail=MySingleNode(None, 1),
                        size=2,
                    ).to_dict()
            ),
            (
                    [1, 2, 3, 4],
                    2,
                    3,
                    MySingleLinkedList(
                        head=MySingleNode(MySingleNode(MySingleNode(MySingleNode(None, 4), 2), 3), 1),
                        tail=MySingleNode(None, 4),
                        size=4,
                    ).to_dict()
            ),
        ]
    )
    def test_swap(self, values_to_add, value_1_to_swap, value_2_to_swap, expected_state):
        instance = MySingleLinkedList()
        for value in values_to_add:
            instance.add_element_at_tail(value=value)
        instance.swap_values(value_1=value_1_to_swap, value_2=value_2_to_swap)
        actual_state = instance.to_dict()
        assert actual_state == expected_state

    @pytest.mark.parametrize(
        'instance',
        [
            (MySingleLinkedList())
        ]
    )
    def test_swap__negative_scenario_empty_collection(self, instance):
        with pytest.raises(EmptyCollection):
            instance.swap_values(value_1=1, value_2=2)

    @pytest.mark.parametrize(
        'values_to_add, value_1_to_swap, value_2_to_swap, ',
        [
            (
                    [1, 2, 3],
                    -1,
                    1,
            ),
            (
                    [1, 2, 3],
                    2,
                    -1,
            ),
        ]
    )
    def test_swap_negative_scenario_values_not_found(
            self,
            values_to_add,
            value_1_to_swap,
            value_2_to_swap,
    ):
        instance = MySingleLinkedList()
        for value in values_to_add:
            instance.add_element_at_tail(value=value)

        with pytest.raises(ValueNotFoundError):
            instance.swap_values(value_1=value_1_to_swap, value_2=value_2_to_swap)


class TestGetNumberOfNodesFunction:
    @pytest.mark.parametrize(
        'head, expected_result',
        [
            (None, 0),
            (MySingleNode(None, 1), 1),
            (MySingleNode(MySingleNode(MySingleNode(None, 3), 100), 1), 3),
        ]
    )
    def test_get_number_of_nodes(self, head, expected_result):
        actual_result = get_number_of_nodes(head=head)
        assert actual_result == expected_result


class TestMyDoubleLinkedList:
    @pytest.mark.parametrize(
        'new_size, expected_result',
        [
            (0, True),
            (1, False),
        ]
    )
    def test_is_empty(self, new_size, expected_result):
        instance = MyDoubleLinkedList()
        instance._size = new_size
        actual_result = instance.is_empty()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'instance',
        [
            MyDoubleLinkedList()
        ]
    )
    def test_first__negative_scenario_empty_collection(
            self, instance,
    ):
        with pytest.raises(EmptyCollection):
            first_element = instance.first

    @pytest.mark.parametrize(
        'values_to_add, expected_value, all_values_from_head, all_values_from_tail',
        [
            (
                    [1],
                    1,
                    [1],
                    [1],
            ),
        ]
    )
    def test_first(self, values_to_add, expected_value, all_values_from_head, all_values_from_tail):
        instance = MyDoubleLinkedList()
        for value in values_to_add:
            instance.insert_first(value)
        actual_result = instance.first
        assert actual_result == expected_value
        assert all_values_from_head == instance.all_values_from_head
        assert all_values_from_tail == instance.all_values_from_tail

    @pytest.mark.parametrize(
        'instance',
        [
            MyDoubleLinkedList()
        ]
    )
    def test_last__negative_scenario_empty_collection(
            self, instance,
    ):
        with pytest.raises(EmptyCollection):
            first_element = instance.last

    @pytest.mark.parametrize(
        'values_to_add, expected_value, all_values_from_head, all_values_from_tail',
        [
            (
                    [1],
                    1,
                    [1],
                    [1],
            ),
        ]
    )
    def test_last(self, values_to_add, expected_value, all_values_from_head, all_values_from_tail):
        instance = MyDoubleLinkedList()
        for value in values_to_add:
            instance.insert_first(value)

        actual_result = instance.last
        assert actual_result == expected_value
        assert all_values_from_head == instance.all_values_from_head
        assert all_values_from_tail == instance.all_values_from_tail

    @pytest.mark.parametrize(
        'values_to_add, all_values_from_head, all_values_from_tail',
        [
            (
                    [1],
                    [1],
                    [1],
            ),
            (
                    [1, 2],
                    [2, 1],
                    [1, 2]
            ),
            (
                    [1, 2, 3],
                    [3, 2, 1],
                    [1, 2, 3],
            ),


            #

        ]
    )
    def test_insert_fist(self, values_to_add, all_values_from_head, all_values_from_tail):
        instance = MyDoubleLinkedList()
        for value in values_to_add:
            instance.insert_first(value)

        assert all_values_from_head == instance.all_values_from_head
        assert all_values_from_tail == instance.all_values_from_tail

    @pytest.mark.parametrize(
        'values_to_add, all_values_from_head, all_values_from_tail',
        [
            (
                    [1],
                    [1],
                    [1],
            ),
            (
                    [1, 2],
                    [1, 2],
                    [2, 1]
            ),
            (
                    [1, 2, 3],
                    [1, 2, 3],
                    [3, 2, 1],
            ),
        ]
    )
    def test_insert_last(self, values_to_add, all_values_from_head, all_values_from_tail):
        instance = MyDoubleLinkedList()
        for value in values_to_add:
            instance.insert_last(value)

        assert all_values_from_head == instance.all_values_from_head
        assert all_values_from_tail == instance.all_values_from_tail

    @pytest.mark.parametrize(
        'instance',
        [
            MyDoubleLinkedList()
        ]
    )
    def test_delete_first__negative_scenario_empty_collection(
            self, instance,
    ):
        with pytest.raises(EmptyCollection):
            first_element = instance.delete_fist()

    @pytest.mark.parametrize(
        'values_to_add, expected_deleted_value, all_values_from_head, all_values_from_tail',
        [
            (
                    [1],
                    1,
                    [],
                    [],
            ),
            (
                    [1, 2],
                    2,
                    [1],
                    [1]
            ),
            (
                    [1, 2, 3],
                    3,
                    [2, 1],
                    [1, 2
                     ],
            ),
        ]
    )
    def test_delete_first(self, values_to_add, expected_deleted_value, all_values_from_head, all_values_from_tail):
        instance = MyDoubleLinkedList()
        for value in values_to_add:
            instance.insert_first(value)

        deleted_value = instance.delete_fist()
        assert deleted_value == expected_deleted_value
        assert all_values_from_head == instance.all_values_from_head
        assert all_values_from_tail == instance.all_values_from_tail

    @pytest.mark.parametrize(
        'instance',
        [
            MyDoubleLinkedList()
        ]
    )
    def test_delete_last__negative_scenario_empty_collection(
            self, instance,
    ):
        with pytest.raises(EmptyCollection):
            first_element = instance.delete_last()

    @pytest.mark.parametrize(
        'values_to_add, expected_deleted_value, all_values_from_head, all_values_from_tail',
        [
            (
                    [1],
                    1,
                    [],
                    [],
            ),
            (
                    [1, 2],
                    1,
                    [2],
                    [2]
            ),
            (
                    [1, 2, 3],
                    1,
                    [3, 2],
                    [2, 3],
            ),
        ]
    )
    def test_delete_last(self, values_to_add, expected_deleted_value, all_values_from_head, all_values_from_tail):
        instance = MyDoubleLinkedList()
        for value in values_to_add:
            instance.insert_first(value)

        deleted_value = instance.delete_last()
        assert deleted_value == expected_deleted_value
        assert all_values_from_head == instance.all_values_from_head
        assert all_values_from_tail == instance.all_values_from_tail
