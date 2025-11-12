"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float) -> float:
    """Exchange budget at exchange rate."""

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Budget remaining after exchanging."""

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculated value of the bills."""

    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Number of bills that can be obtained from the amount."""

    return amount // denomination


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """The amount that is "leftover", given the current denomination."""

    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Maximum value you can get."""

    return get_value_of_bills(
        denomination,
        get_number_of_bills(
            exchange_money(
                budget,
                exchange_rate * (1 + spread / 100)
            ),
            denomination
        )
    )
