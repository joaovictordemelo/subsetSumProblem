from bisect import bisect_left

def subset_sum_mitm(S, T):
    n = len(S)
    left_half = [(0, 0)]
    right_half = [(0, 0)]

    # Split the set S into two halves
    for i in range(n // 2):
        size = len(left_half)
        for j in range(size):
            left_half.append((left_half[j][0] + S[i], left_half[j][1] | 1 << i))

    for i in range(n // 2, n):
        size = len(right_half)
        for j in range(size):
            right_half.append((right_half[j][0] + S[i], right_half[j][1] | 1 << i))

    # Sort the right half by weight
    right_half.sort()

    # Traverse the left half and find the largest weight in the right half
    max_weight = 0
    for i in range(len(left_half)):
        weight, mask = left_half[i]
        complement = T - weight

        # Search for the complement in the right half
        j = bisect_left(right_half, (complement, 0))
        while j < len(right_half) and right_half[j][0] == complement:
            if right_half[j][1] & ~mask:
                max_weight = max(max_weight, weight + right_half[j][0])
            j += 1

    # Return whether a subset sum of T exists in S
    return max_weight >= T
