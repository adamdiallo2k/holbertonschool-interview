#!/usr/bin/python3
"""
    Lockboxes algorithm : can you open all box or not ?
"""

def island_perimeter(grid):
    # Initialize the perimeter count
    perimeter = 0
    
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the four possible sides (up, down, left, right)
                if r == 0 or grid[r - 1][c] == 0:  # Up
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Down
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Right
                    perimeter += 1
    
    return perimeter
