def leap_year(year) -> bool:
    """Returns True if the given year is a leap year, False otherwise."""

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    
    return True