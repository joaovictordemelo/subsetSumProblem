import random

def subset_sum_ftpas(S, T, epsilon):
    n = len(S)
    B = int(epsilon * n * sum(S))

    # Initialize the DP table
    dp = [False] * (2*B+1)
    dp[B] = True

    # Fill in the DP table
    for i in range(n):
        if S[i] > 0:
            for j in range(2*B, S[i]-1, -1):
                dp[j] |= dp[j-S[i]]

    # Search for a subset sum within the approximation factor
    for i in range(T, int((1-epsilon)*T)-1, -1):
        if dp[i+B]:
            return True

    return False

