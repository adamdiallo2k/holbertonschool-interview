#!/usr/bin/python3
"""
    commented function
"""

def makeChange(coins, total):
    """commented function"""
    # If total is 0, no coins are needed
    if total == 0:
        return 0
    
    # If the total is negative, it's impossible to make the change
    if total < 0:
        return -1
    
    # Initialize dp array with a large number, representing infinite coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make 0
    
    # Process each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still float('inf'), it means we cannot make the change
    return dp[total] if dp[total] != float('inf') else -1
