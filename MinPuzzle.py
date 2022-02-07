# Michael Morriss
# Homework 7
# November 15th, 2021


def minEffort_helper(puzzle, m, n, heights, visited):
    """
    Helper function for minEffort(puzzle) method.
    """

    # Returns if row or column is out of bounds or node has been visited.
    if m < 0 or n < 0:
        return 1000
    elif m >= len(puzzle) or n >= len(puzzle[m]):
        return 1000
    elif (m, n) in visited:
        return 1000

    # Adds height of current node to 'heights' list.
    heights.append(puzzle[m][n])

    # Case when bottom right node is reached.
    if m == len(puzzle) - 1:
        if n == len(puzzle[m]) - 1:
            diffs = []
            for i in range(1, len(heights)):
                diffs.append(abs(heights[i] - heights[i - 1]))
            output = max(diffs)
            return output

    # Adds current node to 'visited' list.
    visited.append((m, n))

    # Checks each node before moving onto next.
    return min(
        minEffort_helper(puzzle, m + 1, n, heights, visited),
        minEffort_helper(puzzle, m, n + 1, heights, visited),
        minEffort_helper(puzzle, m - 1, n, heights, visited),
        minEffort_helper(puzzle, m, n - 1, heights, visited)
    )


def minEffort(puzzle):
    """
    Returns the minimal effort integer of a 2D-puzzle.
    """
    return minEffort_helper(puzzle, 0, 0, [], [])

