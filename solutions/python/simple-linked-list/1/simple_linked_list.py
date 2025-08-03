class EmptyListException(Exception):
    def __init__(self, message="The list is empty."):
        super().__init__(message)


class Node:
    def __init__(self, value):
        # Each node stores a song (represented by a number) and a pointer to the next node.
        self._value = value
        self._next = None

    def value(self):
        """Returns the value stored in the node."""
        return self._value

    def next(self):
        """Returns the next node in the linked list."""
        return self._next


class LinkedList:
    def __init__(self, values=None):
        """
        Initializes a linked list.
        If an iterable of values is provided, each value is pushed onto the list.
        Since push adds the new value at the head, the final list order is the reverse of the input.
        For example, LinkedList([1, 2, 3]) creates a list with head value 3.
        """
        self._head = None
        self.count = 0

        if values is not None:
            for value in values:
                self.push(value)

    def __iter__(self):
        """
        Yields each node's value from head to tail.
        This is used when converting the linked list to a list using list(sut).
        """
        current = self._head
        while current:
            yield current.value()
            current = current._next

    def __len__(self):
        """Returns the number of nodes in the linked list."""
        return self.count

    def head(self):
        """
        Returns the head (first node) of the linked list.
        Raises an EmptyListException if the list is empty.
        """
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        """
        Creates a new Node with the given value and adds it to the front of the list.
        This operation is O(1) and updates the count accordingly.
        """
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node
        self.count += 1

    def pop(self):
        """
        Removes the head node from the list and returns its value.
        If the list is empty, an EmptyListException is raised.
        """
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head._next
        self.count -= 1
        return value

    def reversed(self):
        """
        Returns a generator that yields the values of the linked list in reversed order.
        Since this is a singly linked list, the method first collects all node values
        and then yields them in reverse.
        """
        values = list(self)
        for value in reversed(values):
            yield value
