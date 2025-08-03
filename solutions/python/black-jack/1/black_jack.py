"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 if there is no other ace in hand
    3.  '2' - '10' = numerical value.
    """
    # Calculate total value of the current hand
    total = value_of_card(card_one) + value_of_card(card_two)
    
    # Check for the presence of an Ace
    if 'A' in (card_one, card_two):
        return 1  # If there is already an Ace, the new Ace should be 1
    elif total > 10:
        return 1  # If adding another Ace would go over 21
    else:
        return 11  # Otherwise, it is safe to use the Ace as 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt.
    :return: bool - is the hand is a blackjack (two cards worth 21).
    """
    return (card_one == 'A' and card_two in ['10', 'J', 'Q', 'K']) or \
           (card_two == 'A' and card_one in ['10', 'J', 'Q', 'K'])


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two pairs.
    
    A player can split pairs if:
    - Both cards are of the same rank.
    - The cards are a Queen and a King.
    
    :param card_one: str - first card
    :param card_two: str - second card
    :return: bool - True if the hand can be split, False otherwise
    """
    # Check if both cards are the same
    if card_one == card_two:
        return True  # Same value cards can be split
    
    # Check for Q and K being split
    if (card_one == 'Q' and card_two == 'K') or (card_one == 'K' and card_two == 'Q'):
        return True  # Q and K can be split

    return False  # If none of the conditions are met, can't be split


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]