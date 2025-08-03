def total(basket):
    # Price per book in cents
    PRICE = 800

    # Discount mapping: key = number of distinct books in a group,
    # value = discount multiplier (cost = group_size * PRICE * multiplier)
    discounts = {
        1: 1.00,   # no discount
        2: 0.95,   # 5% discount
        3: 0.90,   # 10% discount
        4: 0.80,   # 20% discount
        5: 0.75,   # 25% discount
    }
    
    # Helper function to compute cost for a group with `n` distinct books
    def group_cost(n):
        return int(n * PRICE * discounts[n])
    
    # If the basket is empty, cost is 0.
    if not basket:
        return 0

    # Count the number of copies for each of the 5 possible books.
    counts = [basket.count(i) for i in range(1, 6)]
    
    # Memoization dictionary to cache sub-problem results.
    memo = {}
    
    def best(counts_state):
        # counts_state is a tuple representing the remaining copies of each book.
        if sum(counts_state) == 0:
            return 0
        if counts_state in memo:
            return memo[counts_state]
        
        min_cost = float('inf')
        
        # Try every non-empty subset of the 5 book types.
        # We represent subsets as bit masks from 1 (00001) to 31 (11111)
        for mask in range(1, 1 << 5):
            new_counts = list(counts_state)
            group_size = 0
            valid = True
            # For each book type (position 0 to 4)
            for i in range(5):
                # Check if the i-th book is in this subset.
                if mask & (1 << i):
                    # If no copy is available, then this grouping is not valid.
                    if new_counts[i] == 0:
                        valid = False
                        break
                    new_counts[i] -= 1
                    group_size += 1
                    
            if not valid:
                continue
            
            # Calculate the total cost: cost of this group plus cost for the rest recursively.
            cost_here = group_cost(group_size) + best(tuple(new_counts))
            min_cost = min(min_cost, cost_here)
        
        memo[counts_state] = min_cost
        return min_cost

    return best(tuple(counts))
