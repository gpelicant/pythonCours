"""
NBA Stats with dictionaries
"""


def main():

    players = [
        'Anthony Davis', 'LeBron James', 'James Harden', 'DeMarcus Cousins',
        'Damian Lillard', 'Stephen Curry', 'Devin Booker', 'Russell Westbrook'
    ]
    points = [28.1, 27.5, 30.4, 25.2, 26.9, 26.4, 24.9, 25.4]

    # TODO: Create a dictionary using players and points where players are the
    # keys and values are the points
    stats = dict(zip(players, points))
    # TODO: Call this dictionary `stats` then print it out
    print(stats)
    # NOTE: [Advanced] Take a look at python's `zip` in the Python's doc,
    # that should allow you to
    # implement this in only one line

    # TODO: What was Stephen Curry average points?
    print(stats['Stephen Curry'])
    # TODO: try to print Michael Jordan's average point
    print(stats.get("Michael Jordan's"))
    # YOU SHOULD NOT RAISE AN ERROR!

    # TODO: Which player did score 24.9 ?
    whichPlayer = ''
    for player, point in stats.items():
        if(point == 24.9):
            whichPlayer = player
            break
    print(player)
    # A played is selected if it got a score above 26
    # TODO: Create a dict where keys are the names of the players and values
    #       are True if the player is selected and False otherwise
    playerBoolean = [True if point > 26 else False for player, point in stats.items()]
    stats2 = dict(zip(players, playerBoolean))
    print(stats2)

    # TODO: Build a list of the names of the selected players: selection
    playerSelected = []
    for player, boolean in stats2.items():
        if(boolean == True):
            playerSelected.append(player)
    print(playerSelected)

if __name__ == '__main__':
    main()
