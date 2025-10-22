# Import the heapq library, could not import queue
import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        # Grab the rows and columns lengths of the heights
        rows, cols = len(heights), len(heights[0])

        # Store the efforts to reach a cell
        efforts = []

        # Pre-populate the array with infinity everywhere
        for _ in range(rows):
            row_list = []
            for _ in range(cols):
                row_list.append(float('inf'))
            efforts.append(row_list)

        # Init the starting cell to have 0 effort    
        efforts[0][0] = 0

        # Create a PQ for the open_set and add the start state to the queue
        # This will be the row, column, and effort, respectively
        open_set = [(0, 0, 0)]

        # Explore while the open_set is NOT empty
        while open_set:
            row, col, effort = heapq.heappop(open_set)

            # Stop if the destination is reached
            if row == (rows - 1) and col == (cols - 1):
                return effort

            # Skip if there's already a path found to the current position with less effort
            if effort > efforts[row][col]:
                continue

            # Make the list of moves possible (E, W, N, S)
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            # Iterate over the possible moves
            for dy, dx in moves:
                new_row, new_col = (row + dy, col + dx)

                # Check if the new cell is valid
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate the new effort for this step
                    effort_diff = abs(heights[new_row][new_col] - heights[row][col])

                    # Calculate the max effort to reach the new position
                    new_effort = max(effort, effort_diff)
                    
                    # Check if the new path effort is less effort than currently there
                    if new_effort < efforts[new_row][new_col]:
                        # Change the new position to the new effort found for the path
                        efforts[new_row][new_col] = new_effort

                        # Add the new cell to the open_set
                        heapq.heappush(open_set, (new_row, new_col, new_effort))

        return 0
        
