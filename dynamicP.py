def subset_sum_mitm_dp(S, T):
    n = len(S)
    left_half = [0]
    right_half = [0]

    # Split the set S into two halves
    for i in range(n // 2):
        size = len(left_half)
        for j in range(size):
            left_half.append(left_half[j] + S[i])

    for i in range(n // 2, n):
        size = len(right_half)
        for j in range(size):
            right_half.append(right_half[j] + S[i])

    # Sort the right half by weight
    right_half.sort()

    # Initialize DP array
    dp = [False] * (T+1)
    dp[0] = True

    # Traverse the left half and find the largest weight in the right half
    max_weight = 0
    for i in range(len(left_half)):
        weight = left_half[i]
        complement = T - weight

        # Search for the complement in the right half using binary search
        j = bisect_left(right_half, complement)
        if j < len(right_half) and right_half[j] == complement:
            max_weight = max(max_weight, weight + complement)
        if j > 0 and right_half[j-1] <= complement:
            max_weight = max(max_weight, weight + right_half[j-1])

        # Update DP array
        for t in range(T, weight-1, -1):
            dp[t] |= dp[t - weight]

    # Return whether a subset sum of T exists in S
    return dp[T] or max_weight >= T

