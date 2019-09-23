from typing import Optional, Any, Union, Dict, Callable

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

    # R-7.7 Our CircularQueue class of Section 7.2.2 provides a rotate()
    # method that has semantics equivalent to Q.enqueue(Q.dequeue()),
    # for a nonempty queue.
    # Implement such a method for the LinkedQueue class of Sec- tion 7.1.2 without the creation of any new nodes.
    def rotate(self):
        if len(self) > 1:
            before_old_tail = self._find_node_before_tail()
            old_tail = self._tail

            before_old_tail.next_node = None
            self._tail = before_old_tail

            old_tail.next_node = self._head
            self._head = old_tail

    def _find_node_before_tail(self):
        if len(self) > 1:
            next_node = self._head
            while next_node is not self._tail:
                next_node = next_node.next_node
            return next_node
        return None


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
        self.previous_node = previous_node

        self.next_node = next_node


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
        self._raise_if_empty()
        return self._head.value

    def _raise_if_empty(self):
        if self.is_empty():
            raise EmptyCollection()

    @property
    def last(self):
        self._raise_if_empty()
        return self._tail.value

    def insert_first(self, value: Any):
        if self.is_empty():
            node = MyDoubledLinkedNode(value=value)
            self._tail = node
            self._head = node
        else:
            node = MyDoubledLinkedNode(value=value, next_node=self._head)
            self._head.previous_node = node
            self._head = node

        self._size += 1

    def insert_last(self, value: Any):
        if self.is_empty():
            node = MyDoubledLinkedNode(value=value)
            self._tail = node
            self._head = node
        else:
            node = MyDoubledLinkedNode(value=value, previous_node=self._tail)
            self._tail.next_node = node
            self._tail = node

        self._size += 1

    def delete_fist(self) -> Any:
        self._raise_if_empty()
        value = self._head.value

        if len(self) == 1:
            self._tail = None
        self._head = self._head.next_node
        if self._head:
            self._head.previous_node = None

        self._size -= 1

        return value

    def delete_last(self) -> Any:
        self._raise_if_empty()
        value = self._tail.value

        if len(self) == 1:
            self._head = None
        self._tail = self._tail.previous_node
        if self._tail:
            self._tail.next_node = None

        return value

    # TODO: to follow DRY rule use iterator pattern
    @property
    def all_values_from_head(self):
        current_node = self._head
        all_values = list()
        while current_node:
            all_values.append(current_node.value)
            current_node = current_node.next_node

        return all_values

    @property
    def all_values_from_tail(self):
        current_node = self._tail
        all_values = list()
        while current_node:
            all_values.append(current_node.value)
            current_node = current_node.previous_node

        return all_values

    # R-7.8 Describe a nonrecursive method for finding, by link hopping,
    # the middle node of a doubly linked list with header and trailer sentinels.
    # \In the case of an even number of nodes, report the node slightly left of center as the “middle.”
    # (Note: This method must only use link hopping; it cannot use a counter.)
    # What is the running time of this method?
    def find_middle_value(self):
        slow_pointer = self._head
        fast_pointer = self._head
        while fast_pointer is not None and fast_pointer.next_node is not None:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node

        return slow_pointer.value


# my not the best implementation. The current should point the last element so
# there is no need to iterate to last element to add new one.
# if we have the lest element so in the same time we can get first element
class MyCircularList:
    def __init__(self):
        self._current: Optional[MySingleNode] = None

    # R-7.5 Implement a function that counts the number of nodes in a circularly linked list
    def __len__(self):
        return len(self.get_items())

    def is_empty(self):
        return len(self) == 0

    def add(self, item: Any):
        if self._current:
            next_element = self._current.next_node
            new_node = MySingleNode(next_node=next_element, value=item)
            self._current.next_node = new_node
        else:
            new_node = MySingleNode(next_node=None, value=item)
            new_node.next_node = new_node
            self._current = new_node

    def get_items(self):
        elements = list()
        if self._current:
            next_item = self._current.next_node
            next_item_value = next_item.value
            while self._current is not next_item:
                elements.append(next_item_value)

                next_item = next_item.next_node
                next_item_value = next_item.value

            elements.append(next_item_value)

        return elements


class CircularQueue:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyCollection('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyCollection('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

    # R-7.6 Suppose that x and y are references to nodes of circularly linked lists,
    # although not necessarily the same list.
    # Describe a fast algorithm for telling if x and y belong to the same list.
    def _is_node_belong(self, node: _Node):
        is_belong = False
        if not self.is_empty():
            is_belong = node is self._tail
            next_node = self._tail.next_node
            while not is_belong and next_node is not self._tail:
                is_belong = next_node is node
                next_node = next_node.next_node

        return is_belong

