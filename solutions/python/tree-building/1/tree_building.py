class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    # For an empty list, return None.
    if not records:
        return None

    # Sort records by record_id so that we can validate continuity.
    records.sort(key=lambda record: record.record_id)

    # Ensure that record IDs are continuous and start at 0.
    for expected_id, record in enumerate(records):
        if record.record_id != expected_id:
            raise ValueError("Record id is invalid or out of order.")

    # Create one Node per record using a dictionary for quick lookups.
    nodes = {record.record_id: Node(record.record_id) for record in records}

    # Build the tree and validate parent-child relationships.
    for record in records:
        if record.record_id == 0:
            # Only the root may have parent_id equal to its record_id.
            if record.parent_id != 0:
                raise ValueError("Node parent_id should be smaller than it's record_id.")
            continue

        # Every non-root record must have a parent_id that is less than its record_id.
        if record.parent_id >= record.record_id:
            if record.parent_id == record.record_id:
                raise ValueError("Only root should have equal record and parent id.")
            raise ValueError("Node parent_id should be smaller than it's record_id.")

        # Attach the node to its parent.
        parent_node = nodes[record.parent_id]
        parent_node.children.append(nodes[record.record_id])

    return nodes[0]
