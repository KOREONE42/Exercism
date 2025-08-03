from collections import defaultdict, deque

def can_chain(dominoes):
    """
    Determines if a list of dominoes can be arranged in a circular chain where adjacent dominoes match
    and the chain ends where it started (i.e., forms a loop). Each domino is represented as a tuple (a, b).
    
    Parameters:
    dominoes (list of tuple): A list of domino pieces, each represented as a 2-tuple of integers.

    Returns:
    list of tuple or None: A valid circular domino chain if possible, otherwise None.
    """
    if not dominoes:
        return []

    from collections import defaultdict, deque

    # Step 1: Build the adjacency list (undirected multigraph)
    graph = defaultdict(list)
    degree = defaultdict(int)

    for i, (a, b) in enumerate(dominoes):
        graph[a].append((b, i))
        graph[b].append((a, i))
        degree[a] += 1
        degree[b] += 1

    # Step 2: Check all nodes have even degree (Eulerian circuit requirement)
    if any(deg % 2 != 0 for deg in degree.values()):
        return None

    # Step 3: Check connectivity using BFS
    start = next(iter(graph))  # start from any node with degree > 0
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    # Only consider nodes that are part of the graph (i.e., have edges)
    connected_nodes = {k for k in graph if degree[k] > 0}
    if visited != connected_nodes:
        return None

    # Step 4: Use Hierholzer’s algorithm to find Eulerian circuit
    def find_eulerian_path(u):
        stack, path = [u], []
        local_graph = defaultdict(list)
        used = set()

        # Copy graph to local_graph for in-place edge removals
        for a in graph:
            for b, idx in graph[a]:
                local_graph[a].append((b, idx))

        # Traverse using a stack to build the Eulerian path
        while stack:
            v = stack[-1]
            while local_graph[v]:
                w, idx = local_graph[v].pop()
                edge = tuple(sorted((v, w))) + (idx,)
                if edge in used:
                    continue
                used.add(edge)
                stack.append(w)
                break
            else:
                path.append(stack.pop())

        return path[::-1]

    path = find_eulerian_path(start)

    # Step 5: Convert path to domino sequence
    if len(path) < 2:
        return None

    used_dominoes = [False] * len(dominoes)
    result = []

    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        found = False
        for j, (x, y) in enumerate(dominoes):
            if not used_dominoes[j] and ((x == a and y == b) or (x == b and y == a)):
                used_dominoes[j] = True
                result.append((a, b))
                found = True
                break
        if not found:
            return None

    # Ensure the chain is circular (first and last match)
    if result[0][0] != result[-1][1]:
        return None

    return result
