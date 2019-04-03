"""lib.py

"""


def sum_(seq):
    """
    Returns the sum of a sequence
    """
    # TODO: implement this function
    sumSeq = 0
    for num in seq:
        sumSeq += num
    return sumSeq


def mean(seq):
    """
    Returns the mean of a sequence of numbers
    """
    # TODO: implement this function
    sumSeq = 0
    i = 0
    for num in seq:
        sumSeq += num
        i += 1
    averageValue = sumSeq / i
    return int(averageValue)


def median(seq):
    """
    Returns the median of a sequence of numbers

    Args
    ----
    seq: a sequence (list, tuple, etc..)

    Returns
    -------
    float:
        the median of seq

    >>> median([3, 1, 2])
    2

    >>> median([4, 1, 3, 2])
    2.5
    """
    # TODO: implement this function
    sortedList = sorted(seq)
    lenList = len(seq)
    positionMedian = int(lenList / 2)
    return sortedList[positionMedian]


def mode(seq):
    """
    Returns the most frequent value in a sequence
    If 2 values have the same frequencies, return the smallest one
    """
    # TODO: implement this function


def variance(seq):
    """
    Returns the variance of all elements of a sequence of numbers
    """
    # TODO: implement this function (this one is a bit harder)


def stdev(seq):
    """
    Returns the standard deviation of all elements of a sequence of numbers
    """
    # TODO: implement this function
    # NOTE: Bonus point if you can do it without imports
