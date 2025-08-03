import io

class MeteredFile(io.BufferedRandom):
    """A metered file object that counts the bytes and number of operations
    for both read and write actions.
    
    Implemented using subclassing.
    """
    def __init__(self, *args, **kwargs):
        # Initialize counters.
        self._read_ops = 0
        self._read_bytes = 0
        self._write_ops = 0
        self._write_bytes = 0
        # Initialize the underlying BufferedRandom with given args.
        super().__init__(*args, **kwargs)

    def __enter__(self):
        # Return self as the context-managed object.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Delegate exiting to the underlying implementation.
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        # Return self as an iterator.
        return self

    def __next__(self):
        # Use readline() for each iteration step.
        line = self.readline()
        if not line:
            raise StopIteration
        return line

    def read(self, size=-1):
        data = super().read(size)
        self._read_ops += 1
        self._read_bytes += len(data)
        return data

    def readline(self, size=-1):
        line = super().readline(size)
        self._read_ops += 1
        self._read_bytes += len(line)
        return line

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        n = super().write(b)
        self._write_ops += 1
        self._write_bytes += n
        return n

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """A metered socket wrapper that counts the bytes and number of operations
    for both send and recv. Implemented using delegation.
    """
    def __init__(self, socket):
        self._socket = socket
        self._recv_ops = 0
        self._recv_bytes = 0
        self._send_ops = 0
        self._send_bytes = 0

    def __enter__(self):
        # Simply return self. Do not delegate __enter__.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Delegate __exit__ to the wrapped socket.
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        # Do not check for bufsize None here so that the underlying socket
        # receives the arguments as provided. This allows a call like
        # `recv(None)` to propagate the error from the wrapped socket.
        if not isinstance(flags, int):
            raise TypeError("an integer is required (got type {})".format(type(flags).__name__))
        data = self._socket.recv(bufsize, flags)
        self._recv_ops += 1
        self._recv_bytes += len(data)
        return data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        if not isinstance(flags, int):
            raise TypeError("an integer is required (got type {})".format(type(flags).__name__))
        n = self._socket.send(data, flags)
        self._send_ops += 1
        self._send_bytes += n
        return n

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops
