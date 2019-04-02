#!/usr/bin/env python3
# TODO: Write a docstring
"""
nba stats poupipoupipoupipou
"""

def main():
    players = [
        'Anthony Davis', 'LeBron James', 'James Harden', 'DeMarcus Cousins',
        'Damian Lillard', 'Stephen Curry', 'Devin Booker', 'Russell Westbrook'
    ]
    points = [28.1, 27.5, 30.4, 25.2, 26.9, 26.4, 24.9, 25.4]

    # TODO: print out the total number of points
    total = 0
    for point in points:
        total += point
    print(f'Total number of points: {total}')
    # Example:
    # "Total number of points: 34.3"

    # TODO: print out the player with the biggest average points
    # Example: "Best player: Damian Lillard"
    maxPoint = points.index(max(points))
    bestPlayer = players[maxPoint]
    print(f"Best player: {bestPlayer}")

    # TODO: print out the list of players ordered by descending points
    tuples = list(zip(players, points))
    tri = sorted(tuples, key=lambda tup: tup[1], reverse= True)
    playersSorted, pointsSorted = zip(*tri)
    print(list(playersSorted))

if __name__ == '__main__':
    main()
