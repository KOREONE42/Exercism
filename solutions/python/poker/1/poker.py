from collections import Counter

def best_hands(hands):
    # Evaluate every hand and determine the best value.
    values = [hand_value(hand) for hand in hands]
    best_value = max(values)
    # Return hands that tie for the best value, preserving input order.
    return [hand for hand, value in zip(hands, values) if value == best_value]

def hand_value(hand):
    """Return a tuple (category, tiebreakers) where category is an int (0-8)
    and tiebreakers is a tuple of numbers for comparing hands.
    
    Categories:
      8: Straight flush
      7: Four-of-a-kind
      6: Full house
      5: Flush
      4: Straight
      3: Three-of-a-kind
      2: Two pairs
      1: One pair
      0: High card
    """
    # Parse the hand into card ranks and suits.
    cards = hand.split()
    ranks = []
    suits = []
    for card in cards:
        # card[:-1] works both for "10D" and "JH", etc.
        rank_str, suit = card[:-1], card[-1]
        suits.append(suit)
        if rank_str == 'A':
            value = 14
        elif rank_str == 'K':
            value = 13
        elif rank_str == 'Q':
            value = 12
        elif rank_str == 'J':
            value = 11
        else:
            value = int(rank_str)
        ranks.append(value)
    
    # Check for flush: all cards same suit.
    flush = len(set(suits)) == 1

    # Sort the card values.
    sorted_ranks = sorted(ranks)
    
    # Check for a straight.
    # Normal case: five consecutive values.
    if sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0] + 5)):
        straight = True
        # High card is the last in order.
        straight_high = sorted_ranks[-1]
    # Special case: Ace can be low, so A,2,3,4,5 is valid.
    elif sorted_ranks == [2, 3, 4, 5, 14]:
        straight = True
        # Ace is counted as low; high card is 5.
        straight_high = 5
    else:
        straight = False

    # Count occurences of each rank.
    counter = Counter(ranks)
    # Create groups sorted by count (descending), then by rank value (descending).
    groups = sorted(counter.items(), key=lambda item: (item[1], item[0]), reverse=True)

    # Determine category and tie-breaker tuple.
    # Category order (from lowest (0) to highest (8)):
    # 0: High card, 1: One pair, 2: Two pairs, 3: Three-of-a-kind,
    # 4: Straight, 5: Flush, 6: Full house, 7: Four-of-a-kind, 8: Straight flush.
    if flush and straight:
        category = 8
        tiebreaker = (straight_high,)
    elif groups[0][1] == 4:
        # Four-of-a-kind: rank of quadruple, then kicker.
        four_val = groups[0][0]
        kicker = [r for r in ranks if r != four_val][0]
        category = 7
        tiebreaker = (four_val, kicker)
    elif groups[0][1] == 3 and groups[1][1] == 2:
        # Full house: triplet rank, then pair rank.
        category = 6
        tiebreaker = (groups[0][0], groups[1][0])
    elif flush:
        # Flush: use descending order of all cards.
        category = 5
        tiebreaker = tuple(sorted(ranks, reverse=True))
    elif straight:
        category = 4
        tiebreaker = (straight_high,)
    elif groups[0][1] == 3:
        # Three-of-a-kind: triplet then the kickers in descending order.
        triple = groups[0][0]
        kickers = sorted([r for r in ranks if r != triple], reverse=True)
        category = 3
        tiebreaker = (triple,) + tuple(kickers)
    elif groups[0][1] == 2 and len(groups) >= 2 and groups[1][1] == 2:
        # Two pairs: compare the higher pair, then the lower pair, then the kicker.
        pair1, pair2 = groups[0][0], groups[1][0]
        # Ensure the highest pair is first.
        high_pair, low_pair = max(pair1, pair2), min(pair1, pair2)
        kicker = [r for r in ranks if r != pair1 and r != pair2][0]
        category = 2
        tiebreaker = (high_pair, low_pair, kicker)
    elif groups[0][1] == 2:
        # One pair: pair then kickers in descending order.
        pair = groups[0][0]
        kickers = sorted([r for r in ranks if r != pair], reverse=True)
        category = 1
        tiebreaker = (pair,) + tuple(kickers)
    else:
        # High card: compare all cards in descending order.
        category = 0
        tiebreaker = tuple(sorted(ranks, reverse=True))
    
    return (category, tiebreaker)
