import math
from collections import deque

def measure(bucket_one, bucket_two, goal, start_bucket):
    """
    Determine the sequence of actions to measure exactly `goal` liters using two buckets.

    Args:
        bucket_one (int): capacity of the first bucket ("one").
        bucket_two (int): capacity of the second bucket ("two").
        goal (int): desired volume to measure.
        start_bucket (str): which bucket to fill first, either 'one' or 'two'.

    Returns:
        tuple: (actions, goal_bucket, other_bucket_amount)
            actions (int): total number of actions taken (including initial fill).
            goal_bucket (str): 'one' or 'two', the bucket containing the goal.
            other_bucket_amount (int): liters left in the other bucket.

    Raises:
        ValueError: if the goal cannot be reached or invalid inputs.
    """
    # Validate inputs
    if start_bucket not in ('one', 'two'):
        raise ValueError("start_bucket must be 'one' or 'two'")
    max_cap = max(bucket_one, bucket_two)
    if goal > max_cap:
        raise ValueError(f"Goal {goal} cannot be greater than both bucket sizes.")
    # Check reachability by gcd
    g = math.gcd(bucket_one, bucket_two)
    if goal % g != 0:
        raise ValueError(f"Goal {goal} is not a multiple of gcd({bucket_one}, {bucket_two})={g}.")

    # Determine initial state
    if start_bucket == 'one':
        start_idx = 0  # corresponds to bucket_one
        capacities = (bucket_one, bucket_two)
        init = (bucket_one, 0)
        forbidden = (0, bucket_two)
    else:
        start_idx = 1
        capacities = (bucket_one, bucket_two)
        init = (0, bucket_two)
        forbidden = (bucket_one, 0)

    # If immediate solution
    if init[0] == goal:
        return (1, 'one', init[1])
    if init[1] == goal:
        return (1, 'two', init[0])

    # BFS to find shortest sequence avoiding forbidden
    visited = set([init])
    queue = deque([(init[0], init[1], 1)])  # (a, b, actions)

    while queue:
        a, b, actions = queue.popleft()
        # All possible moves
        neighbors = []
        cap1, cap2 = capacities
        # Fill bucket one
        neighbors.append((cap1, b))
        # Fill bucket two
        neighbors.append((a, cap2))
        # Empty bucket one
        neighbors.append((0, b))
        # Empty bucket two
        neighbors.append((a, 0))
        # Pour one to two
        transfer = min(a, cap2 - b)
        neighbors.append((a - transfer, b + transfer))
        # Pour two to one
        transfer = min(b, cap1 - a)
        neighbors.append((a + transfer, b - transfer))

        for na, nb in neighbors:
            state = (na, nb)
            # Skip visited
            if state in visited:
                continue
            # Skip forbidden state
            if state == forbidden:
                continue
            # New action count
            nactions = actions + 1
            # Check goal
            if na == goal or nb == goal:
                goal_bucket = 'one' if na == goal else 'two'
                other_amount = nb if na == goal else na
                return (nactions, goal_bucket, other_amount)
            # Enqueue
            visited.add(state)
            queue.append((na, nb, nactions))

    # If BFS completes without finding
    raise ValueError(f"Unable to reach goal {goal} with given buckets.")
