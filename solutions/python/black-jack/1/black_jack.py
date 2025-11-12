"""Functions to help play and score a game of blackjack."""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card."""

    match card:
        case "J" | "Q" | "K":
            return 10
        case "A":
            return 1
        case _:
            return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand."""

    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)

    if val1 > val2:
        return card_one
    elif val2 > val1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card."""

    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    
    return 1 if val1 == 1 or val2 == 1 else 11 if val1 + val2 <= 10 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'."""

    return (value_of_card(card_one) == 10 and value_of_card(card_two) == 1 or 
            value_of_card(card_one) == 1 and value_of_card(card_two) == 10)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands."""

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    
    return False


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet."""

    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    total  = val1 + val2
    
    return total == 9 or total == 10 or total == 11
