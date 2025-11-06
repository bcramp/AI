# Need to import functools to grab the lru_cache
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Grab the length of the array to find the number of piles
        numOfPiles = len(piles)

        # Initialize M=1
        M = 1

        # Initialize an array to keep track of all the following piles added onto each other 
        # from that position. Need numOfPiles + 1 to stay in bounds
        maxStonesFromPos = [0] * (numOfPiles + 1)

        # Create the range values
        startPos = numOfPiles - 1
        stopPos = -1
        step = -1

        # In reverse order, populate the sum of each of the piles from the current position
        for i in range(startPos, stopPos, step):
            # Add the following positions to the current position to get the total number of stones
            # from that position
            maxStonesFromPos[i] = maxStonesFromPos[i + 1] + piles[i]

        # Create an inner function to access the numOfPiles, maxStonesFromPos, call dfs, and 
        # not pass unhashable list.
        @lru_cache(None)
        def minimax(isAlice, pos, m):
            # No piles remaining from current position
            if pos >= numOfPiles:
                return 0

            # Alice is the maximizing player, so check if it's her turn
            if isAlice:
                # Alice's max amount of points
                maxPoints = -float('inf')

                # Alice has the choice between piles 1-2*m
                for pileIdx in range(1, (2*m + 1)):
                    # Calculate the current position and the pile index
                    currPileIdx = pos + pileIdx

                    # If the current pile does not exceed the number of piles
                    if currPileIdx <= numOfPiles:
                        # Number of stones Alice can get
                        aliceStones = maxStonesFromPos[pos] - maxStonesFromPos[currPileIdx]

                        # Alice's maximized points based on Bob's next turn
                        maxPoints = max(maxPoints, aliceStones + minimax(False, currPileIdx, max(m, pileIdx)))

                # Return the max amount of points Alice can get
                return maxPoints
            else:
                # Alice's min points once Bob has tried to minimize
                minPoints = float('inf')

                # Bob has the choice between piles 1-2*m
                for pileIdx in range(1, (2*m + 1)):
                    # Calculate the current position and the pile index
                    currPileIdx = pos + pileIdx

                    # If the current pile does not exceed the number of piles
                    if currPileIdx <= numOfPiles:
                        # Alice's minimized points based on Bob's current turn of minimizing her points
                        minPoints = min(minPoints, minimax(True, currPileIdx, max(m, pileIdx)))
                
                # Return the min amount of points Alice can get since Bob has minimized what she can get
                return minPoints

        # Return Alice's max points she could get
        return minimax(True, 0, M)
