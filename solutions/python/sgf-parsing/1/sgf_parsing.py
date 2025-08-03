class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string:
        raise ValueError("tree missing")
    n = len(input_string)
    i = 0  # index into input_string

    def error(msg):
        raise ValueError(msg)

    # Parse a tree: "(" Sequence { Tree } ")".
    def parse_tree():
        nonlocal i
        if i >= n or input_string[i] != '(':
            error("tree missing")
        i += 1  # consume '('

        nodes = parse_sequence()
        if not nodes:
            error("tree with no nodes")
        # Parse variations (subtrees) that are children of the last node in the sequence.
        children = []
        while i < n and input_string[i] == '(':
            children.append(parse_tree())
        if i >= n or input_string[i] != ')':
            error("tree missing")
        i += 1  # consume ')'
        # Chain the sequence nodes so that each node (if more than one) is the parent of the next.
        root = nodes[0]
        current = root
        for next_node in nodes[1:]:
            current.children.append(next_node)
            current = next_node
        # Attach variations to the last node.
        current.children.extend(children)
        return root

    # Parse a sequence of nodes (one or more) that start with semicolons.
    def parse_sequence():
        nonlocal i
        nodes = []
        while i < n and input_string[i] == ';':
            nodes.append(parse_node())
        return nodes

    # Parse a node: a semicolon and zero or more properties.
    def parse_node():
        nonlocal i
        if i >= n or input_string[i] != ';':
            error("tree missing")
        i += 1  # consume ';'
        node = SgfTree()
        # Parse properties while the current character is an alphabet letter.
        while i < n and input_string[i].isalpha():
            key, values = parse_property()
            node.properties[key] = values
        return node

    # Parse a property: key must be all uppercase and be followed by one or more property values.
    def parse_property():
        nonlocal i
        start = i
        while i < n and input_string[i].isalpha():
            if not input_string[i].isupper():
                error("property must be in uppercase")
            i += 1
        key = input_string[start:i]
        # A key must be immediately followed by at least one '['.
        if i >= n or input_string[i] != '[':
            error("properties without delimiter")
        values = []
        # Multiple values possible for one key.
        while i < n and input_string[i] == '[':
            values.append(parse_property_value())
        return key, values

    # Parse a property value: process escapes, remove newlines after escapes,
    # and convert all whitespace (except newline) to space.
    def parse_property_value():
        nonlocal i
        if i >= n or input_string[i] != '[':
            error("properties without delimiter")
        i += 1  # consume '['
        value_chars = []
        while i < n:
            char = input_string[i]
            if char == ']':
                i += 1  # consume the closing bracket
                break
            elif char == '\\':
                i += 1  # move past backslash
                if i >= n:
                    break
                next_char = input_string[i]
                # If the character immediately after '\' is a newline, skip it.
                if next_char == '\n':
                    i += 1
                    continue
                # For any whitespace (other than newline) encountered via escape, convert to a space.
                if next_char.isspace() and next_char != '\n':
                    value_chars.append(' ')
                else:
                    value_chars.append(next_char)
                i += 1
            else:
                # Convert any whitespace (except newline) to a space.
                if char.isspace() and char != '\n':
                    value_chars.append(' ')
                else:
                    value_chars.append(char)
                i += 1
        else:
            error("properties without delimiter")
        return "".join(value_chars)

    if input_string[i] != '(':
        error("tree missing")
    root = parse_tree()
    if i != n:
        if input_string[i:].strip():
            error("tree missing")
    return root
