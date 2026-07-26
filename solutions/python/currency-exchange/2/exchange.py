"""Functions for calculating steps in exchanging currency.
"""


def exchange_money(budget, exchange_rate) -> float:
    """Calculate estimated value after exchange.
    Parameters:
        budget (float): The amount of money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.
    Returns:
        float: The exchanged value of the foreign currency you can receive.

    This function calculates and returns the (estimated) value of the exchanged currency.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value) -> float:
    """Calculate currency left after an exchange.
    Parameters:
        budget (float): The amount of money you own.
        exchanging_value (float): The amount of your money you want to exchange now.
    Returns:
        float: The amount left of your starting currency after the exchange

    This function calculates and returns the amount of money left over from the budget
    after an exchange.
    """

    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills) -> int:
    """Calculate the total value of currency at current denomination.
    Parameters:
        denomination (int): The value of a single unit (bill).
        number_of_bills (int): The total number of units (bills).
    Returns:
        int: Calculated value of the units (bills).

    This function calculates and returns the total value of the bills (excluding fractional amounts).
    """

    return denomination * number_of_bills


def get_number_of_bills(amount:float, denomination:int) -> int:
    """Calculate the number of currency units (bills) within the amount.
    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).
    Returns:
        int: The number of units (bills) that can be obtained from the amount.

    This function calculates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractional amounts.
    """

    return amount // denomination


def get_leftover_of_bills(amount:float, denomination:int) -> float:
    """Calculate leftover amount after exchanging into bills.
    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).
    Returns:
        float: The amount that is "leftover", given the current denomination.
   
    This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination.
    """

    return amount % denomination


def exchangeable_value(budget:float, exchange_rate:float, spread:int, denomination:int) -> int:
    """Calculate the maximum value of the new currency.
    Parameters:
        budget (float): The amount of your money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.
        spread (int): The percentage that is taken as an exchange fee.
        denomination (int) The value of a single unit (bill).
    Returns:
        int: The maximum value you can get in the new currency.

    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """
    
    actual_exchange = (exchange_rate * spread / 100) + exchange_rate
    new_calc = exchange_money(budget, actual_exchange)
    expected = get_leftover_of_bills(new_calc, denomination)
    return int(new_calc - expected)
