"""
Data utilities
"""


# TODO: implement `load_data` as described in the documentation
def load_data(filepath):
    """
    function load data
    arg
        filepath as a string
    return
        data
    """
    f = open(filepath, "r")
    if f.mode == 'r':
        data = f.read()
        return data

# TODO: implement `file_stats` as described in the documentation
def file_stats(filepath):
    """
    function file stat
    arg
        filepath as a string
    return
        num_lines as a number
        num_words as a number
        num_chars as a number
    """

    stats = {
        'num_words': 0,
        'num_lines': 0,
        'num_chars': 0
    }


    with open(filepath, 'r') as file:
        for line in file:
            stats['num_words'] += len(line.split())
            stats['num_lines'] += 1
            for letters in line:
                stats['num_chars'] += len(letters)
    return stats