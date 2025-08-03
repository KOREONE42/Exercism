class Node:
    def __init__(self, value, succeeding=None, previous=None):
        """A node in a doubly linked list."""
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        """Add a node with the given value to the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        """Remove and return the value from the end of the list. Raise IndexError if empty."""
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.tail.value
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.succeeding.previous = None  # break backward link of removed node
            self.tail.succeeding = None
        self.length -= 1
        return value

    def unshift(self, value):
        """Add a node with the given value to the beginning of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def shift(self):
        """Remove and return the value from the beginning of the list. Raise IndexError if empty."""
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.succeeding
            self.head.previous.succeeding = None  # break forward link of removed node
            self.head.previous = None
        self.length -= 1
        return value

    def delete(self, value):
        """Delete the first node with the given value. Raise ValueError if not found."""
        current = self.head
        while current:
            if current.value == value:
                # Node is head
                if current is self.head:
                    self.shift()
                # Node is tail
                elif current is self.tail:
                    self.pop()
                else:
                    # Bypass current
                    prev_node = current.previous
                    next_node = current.succeeding
                    prev_node.succeeding = next_node
                    next_node.previous = prev_node
                    self.length -= 1
                return
            current = current.succeeding
        raise ValueError("Value not found")

    def __len__(self):
        """Return the number of nodes in the list."""
        return self.length

    def __iter__(self):
        """Iterate over the values in the list from head to tail."""
        current = self.head
        while current:
            yield current.value
            current = current.succeeding
