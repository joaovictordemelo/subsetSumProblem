def subset_sum_meet_in_the_middle(S, target):
    n = len(S)
    half = n // 2

    # Compute all subsets of the first half of S
    sums = {0}
    for i in range(half):
        sums |= {x + S[i] for x in sums}

    # Check if a subset of the second half sums to the remaining target
    for j in range(half, n):
        if target - S[j] in sums:
            return True

    # Compute all subsets of the second half of S
    sums = {0}
    for i in range(half, n):
        sums |= {x + S[i] for x in sums}

    # Check if a subset of the first half sums to the remaining target
    for i in range(half):
        if target - S[i] in sums:
            return True

    # No subset sums to the target
    return False

