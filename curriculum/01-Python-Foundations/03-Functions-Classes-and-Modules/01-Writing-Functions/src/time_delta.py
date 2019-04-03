"""
Timedelta
"""


# TODO: implement readable_timedelta
def readable_timedelta(days):
    """ Return the day and week from days.

    Args
    ----
    days: integer

    Returns
    -------
    a string
    """
    return(f"{int(days / 7)} week(s) and {int(days % 7)} day(s)")