class BufferFullException(BufferError):
    """
    Exception raised when the CircularBuffer is full and a write operation is attempted.
    
    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """
    Exception raised when the CircularBuffer is empty and a read operation is attempted.
    
    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    """
    A circular (ring) buffer that uses a fixed-size list to store data in a FIFO manner.
    
    Methods:
        read() -> Reads and removes the oldest item from the buffer.
        write(data) -> Adds a new item to the buffer; raises BufferFullException if full.
        overwrite(data) -> Adds a new item, overwriting the oldest if buffer is full.
        clear() -> Empties the buffer completely.
    """

    def __init__(self, capacity):
        """
        Initialize the circular buffer with a given capacity.
        
        Args:
            capacity (int): Maximum number of items the buffer can hold.
        """
        self.capacity = capacity
        self.buffer = [None] * capacity  # Fixed-size list to store elements
        self.head = 0  # Index for the next read operation
        self.tail = 0  # Index for the next write operation
        self.size = 0  # Current number of items in the buffer

    def read(self):
        """
        Reads and removes the oldest item from the buffer.
        
        Returns:
            The oldest item in the buffer.
        
        Raises:
            BufferEmptyException: If the buffer is empty.
        """
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")

        value = self.buffer[self.head]  # Get the oldest value
        self.buffer[self.head] = None  # Clear the slot
        self.head = (self.head + 1) % self.capacity  # Move head forward
        self.size -= 1  # Decrease buffer size
        return value

    def write(self, data):
        """
        Writes a new item to the buffer.
        
        Args:
            data: The item to be added to the buffer.
        
        Raises:
            BufferFullException: If the buffer is already full.
        """
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.tail] = data  # Write at the tail index
        self.tail = (self.tail + 1) % self.capacity  # Move tail forward
        self.size += 1  # Increase buffer size

    def overwrite(self, data):
        """
        Overwrites the oldest item if the buffer is full; otherwise behaves like write().
        
        Args:
            data: The item to be added to the buffer.
        """
        if self.size == self.capacity:
            # Overwrite oldest element and advance both tail and head
            self.buffer[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            self.head = (self.head + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        """
        Empties the buffer completely, resetting it to an initial state.
        """
        self.buffer = [None] * self.capacity  # Reset buffer storage
        self.head = 0  # Reset read index
        self.tail = 0  # Reset write index
        self.size = 0  # Reset current size
