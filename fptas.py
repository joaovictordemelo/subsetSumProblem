def fptas_subset_sum(S, target, epsilon):
    n = len(S)
    T = sum(S)
    factor = (epsilon * T) / n
    # Scale down the input set S by factor
    S_scaled = [int(si / factor) for si in S]

    # Compute the DP table
    M = int(n * T / factor) + 1
    dp_table = [[False] * M for _ in range(n)]
    for j in range(S_scaled[0], M):
        dp_table[0][j] = (S_scaled[0] == j)

    for i in range(1, n):
        for j in range(M):
            if S_scaled[i] > j:
                dp_table[i][j] = dp_table[i-1][j]
            else:
                dp_table[i][j] = dp_table[i-1][j] or dp_table[i-1][j-S_scaled[i]]

    # Check if there is a subset of S that adds up to target
    return dp_table[n-1][int(target / factor)]
