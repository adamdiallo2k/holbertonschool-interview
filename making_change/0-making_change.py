#!/usr/bin/python3
"""
    commented function
"""

def makeChange(coins, total):
    """commented function"""
    # If total is 0, no coins are needed
   
    if total <= 0:
        return 0

    # init solutions array with "infinity" value
    # index: amount, value:minimum number coins needed
    solutions = [total + 1] * (total + 1)
    solutions[0] = 0

    # build solution bottom-up
    for m in range(1, total + 1):
        # try each coins
        for c in coins:
            if c <= m:
                # update solution
                solutions[m] = min(solutions[m], 1 + solutions[m - c])

    return solutions[total] if solutions[total] <= total else - 1
