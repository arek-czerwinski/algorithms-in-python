from typing import Optional, Any, Union, Dict

from utils.errors import EmptyCollection


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
        if instance.is_empty():
            return self
        if self.is_empty():
            return instance
        tail = self._tail
        tail.next_node = instance._head
        self._tail = instance._tail
        self._size += instance._size
        return self


# R-7.3 Describe a recursive algorithm that counts the number of nodes in a singly linked list.
def get_number_of_nodes(head: Optional[MySingleNode] = None):
    counter = 0
    while head:
        counter += 1
        head = head.next_node

    return counter
