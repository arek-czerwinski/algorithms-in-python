from typing import Optional, Any, Union, Dict

from utils.errors import EmptyCollection, ValueNotFoundError


class ToDictMixin:
    def to_dict(self):
        dictionary = {
            key: self._convert_value_to_dict_if_needed(value=value)
            for key, value in vars(self).items()
        }
        return dictionary

    @staticmethod
    def _convert_value_to_dict_if_needed(value: Any) -> Union[Dict[str, Any], Any]:
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        return value


class MySingleNode(ToDictMixin):
    def __init__(self, next_node: Optional['MySingleNode'], value: Any) -> None:
        self.next_node = next_node
        self.value = value

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, MySingleNode):
            return False
        return self.next_node == o.next_node and self.value == o.value


class MySingleLinkedList(ToDictMixin):
    def __init__(
            self,
            head: Optional[MySingleNode] = None,
            tail: Optional[MySingleNode] = None,
            size: Optional[int] = 0,
    ) -> None:
        self._head: Optional[MySingleNode] = head or None
        self._tail: Optional[MySingleNode] = tail or None
        self._size = size
        # should be added validation of input values, for example incorrect size to number of nodes

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    @property
    def first(self) -> Any:
        if self.is_empty():
            raise EmptyCollection('No values to get!')
        return self._head.value

    def get_first_and_remove(self):
        if self.is_empty():
            raise EmptyCollection()

        value = self.first
        if len(self) == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next_node
        self._size -= 1
        return value

    def add_element_at_tail(self, value: Any):
        if self.is_empty():
            node = MySingleNode(next_node=None, value=value)
            self._head = node
            self._tail = node
        else:
            node = MySingleNode(next_node=None, value=value)
            tail = self._tail
            tail.next_node = node
            self._tail = node

        self._size += 1

    # R-7.1 Give an algorithm for finding the second-to-last node in a singly linked list in which the last node
    # is indicated by a next reference of None.
    @staticmethod
    def _get_all_values(node: Optional[MySingleNode] = None):
        values = list()
        while node:
            values.append(node.value)
            node = node.next_node

        return values

    def get_all_values(self):
        if self.is_empty():
            return list()
        return [self._head.value] + self._get_all_values(node=self._head.next_node)

    # R - 7.2
    # Describe a good algorithm for concatenating two singly linked lists L and M, given only references to the
    # first node of each list, into a single list L that contains all the nodes of L followed by all the nodes of M.
    def extend(self, instance: 'MySingleLinkedList'):
        # TODO: add creating new instance
        if instance.is_empty():
            return self
        if self.is_empty():
            return instance
        tail = self._tail
        tail.next_node = instance._head
        self._tail = instance._tail
        self._size += instance._size
        return self

    # R-7.4
    # Describe in detail how to swap two nodes x and y (and not just their contents) in a singly
    # linked list L given references only to x and y.
    # Repeat this exercise for the case when L is a doubly linked list. Which algorithm takes more time?
    def swap_values(self, value_1, value_2):
        if self.is_empty():
            raise EmptyCollection()
        if value_1 != value_2:
            # TODO: this code can be improved to find value_1 and value_2 in one iteration
            previous_value_1, current_value_1 = self._get_nodes_based_on_value(
                value=value_1,
                head=self._head,
            )
            previous_value_2, current_value_2 = self._get_nodes_based_on_value(
                value=value_2,
                head=self._head,
            )

            if previous_value_1 is None:
                self._head = current_value_2
            else:
                previous_value_1.next_node = current_value_2

            if previous_value_2 is None:
                self._head = current_value_1
            else:
                previous_value_2.next_node = current_value_1

            tmp_next_node_for_value_2 = current_value_2.next_node
            current_value_2.next_node = current_value_1.next_node
            current_value_1.next_node = tmp_next_node_for_value_2

            if current_value_1.next_node is None:
                self._tail = current_value_1

            if current_value_2.next_node is None:
                self._tail = current_value_2

    def _get_nodes_based_on_value(self, value: Any, head: Optional[MySingleNode] = None):
        previous = None
        current_node = head
        while current_node:
            if current_node.value == value:
                break
            else:
                previous = current_node
                current_node = current_node.next_node

        if current_node is None:
            raise ValueNotFoundError(f'Value {value} not found in {self.get_all_values()}')
        return previous, current_node


# R-7.3 Describe a recursive algorithm that counts the number of nodes in a singly linked list.
def get_number_of_nodes(head: Optional[MySingleNode] = None):
    counter = 0
    while head:
        counter += 1
        head = head.next_node

    return counter


class MyDoubledLinkedNode:
    def __init__(
            self,
            value: Any,
            previous_node: Optional['MyDoubledLinkedNode'] = None,
            next_node: Optional['MyDoubledLinkedNode'] = None,
    ) -> None:
        self.value = value
        self.previous_node = previous_node,
        self._next_node = next_node


class MyDoubleLinkedList:
    def __init__(
            self,
            head: Optional[MyDoubledLinkedNode] = None,
            tail: Optional[MyDoubledLinkedNode] = None,
            size: int = 0,
    ) -> None:
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    @property
    def first(self):
        if self.is_empty():
            raise EmptyCollection()
        return self._head.value

    @property
    def last(self):
        pass

    def insert_first(self, value: Any):
        pass

    def insert_last(self, value: Any):
        pass

    def delete_fist(self) -> Any:
        pass

    def delete_last(self) -> Any:
        pass
