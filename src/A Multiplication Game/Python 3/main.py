"""
In combinatorial game theory, a N-position is a position from whom
the next player to move wins if he plays perfectly. A P-position is
a position where the next player to move always loses if his opponen
plays perfectly.

Recursively we can define them as:
    A position is a N-position if it can move to a P-position
    A position is a P-position if it can only move to N-positions
Given that we usually know the end condition of the game and who wins,
we can work our way backwards and find the type of the initial position.

All values n and above are P-positions.

The lowest position we can reach n is z=ceil(n/9) so all positions 
[z,z+1,...,n-1] must be N positions.

The only positions that are forced to move to [z,z+1,...,n-1] are those
that when multiplied by 2 land in that interval, that is given w = ceil(z/2),
we conclude [w,w+1,...,z-1] are all P-positions.

We can continue like this until we find an interval containing 1. If 1 is a N
position, than Stan wins, otherwise Ollie does.

Note that the value of positions is determined by the value of n so we can't
memorize positions from one game to another. We could however memorize interval
and type of position pairs but given that this has logarithmic complexity and
guessing that cache hits are somewhat unlikely in a 30 at most lines scenario,
I doubt it is worth it.

Also note that if we are not thinking about memorizing intervals, there is no 
need to care about the interval as such, just its lower bound.
"""

import sys
from math import ceil

def winner(n):
    player = True
    while n>1:
        d,m = divmod(n,(9 if player else 2))
        n = d+1 if m else d
        player = not player
    return 'Ollie wins.' if player else 'Stan wins.' 

def main():
    print('\n'.join(winner(int(line)) for line in sys.stdin.readlines()))

if __name__ == "__main__":
    main()