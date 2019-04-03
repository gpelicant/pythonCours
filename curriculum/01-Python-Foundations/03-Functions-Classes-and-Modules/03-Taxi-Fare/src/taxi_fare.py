"""
Taxi Fare

A module that implements a function to compute the fare of a taxi trip.
"""


# TODO: implement the compute_fare function.
# NOTE: Don't forget to write a nice docstring

def compute_fare(distance, duration, drop_charge=2.60):
    """
    Returns the compute fare of a taxi.

    Args
    ----
    distance: float
    duration: float
    drop_charge: float

    Returns
    -------
    a float
    """
    distancePerMiles = 2.70
    durationPerMinute = 0.50
    calculDuration = duration * durationPerMinute
    calculDistance = distance * distancePerMiles
    total = drop_charge + calculDistance + calculDuration
    return total