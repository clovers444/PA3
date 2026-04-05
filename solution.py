def max_value_common_subsequence(K, char_values, A, B):
    n = len(A)
    m = len(B)

    # Create a 2D array to store the maximum value of common subsequence at each point
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, add the value of the character to the result from the previous indices
            if A[i - 1] == B[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + char_values.get(A[i - 1], 0)
            # If characters do not match, take the maximum value from either the left or the top cell
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # Backtrack to find the actual longest common subsequence
    result = []
    i, j = n, m

    while i > 0 and j > 0:
        # If characters match, add it to the result and move diagonally up-left
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1]) 
            i -= 1
            j -= 1
        # If characters do not match, move in the direction of the maximum value
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        # If the values are equal, we can move in either direction (here we choose to move left)
        else:
            j -= 1

    result.reverse()
    return dp[n][m], ''.join(result)