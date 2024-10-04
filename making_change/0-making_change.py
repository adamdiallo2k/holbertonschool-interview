#!/usr/bin/python3
"""
    commented function
"""

def makeChange(coins, total):
    """commented function"""
    # If total is 0, no coins are needed
    if total < 0:
        return -1
    if total == 0:
        return 0

    # Create an array to store the minimum coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins are needed for the total of 0

    # Iterate through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
