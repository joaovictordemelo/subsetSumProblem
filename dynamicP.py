def subset_sum_dp(S, target):
    n = len(S)
    # Initialize the table with False values
    table = [[False] * (target + 1) for _ in range(n + 1)]

    # Initialize the first column as True
    for i in range(n + 1):
        table[i][0] = True

    # Fill the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # If the current element is greater than the target sum,
            # we can't include it in any subset
            if S[i - 1] > j:
                table[i][j] = table[i - 1][j]
            # Otherwise, we have two choices:
            # 1. Include the current element in the subset
            # 2. Exclude the current element from the subset
            else:
                table[i][j] = table[i - 1][j] or table[i - 1][j - S[i - 1]]

    # The target sum is achievable if and only if there is a subset
    # of S that sums to the target
    return table[n][target]
