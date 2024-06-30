def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Example usage
weights = [1,3,5,4,1,3,2]
values = [5,10,15,7,8,9,4]
capacity = 8
print(knapsack(weights, values, capacity))  # Output: 32
