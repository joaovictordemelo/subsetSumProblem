from collections import Counter


def prime_factorization_subset_sum(S, T):
    # Step 1: Get the set of distinct prime factors in S
    P = set()
    for num in S:
        prime_factors = prime_factorization(num)
        for factor in prime_factors:
            P.add(factor)
    
    # Step 2: Group elements in S by their prime factorization
    group_dict = {}
    for num in S:
        prime_factors = prime_factorization(num)
        group = tuple([prime_factors.get(p, 0) for p in P])
        group_dict.setdefault(group, []).append(num)
    
    # Step 3: Compute subset sum for each group
    dp = [False] * (T + 1)
    dp[0] = True
    for group in group_dict.values():
        # Compute unique prime factorizations in group
        U = set([tuple([prime_factorization(num).get(p, 0) for p in P]) for num in group])
        
        # Compute subset sum for each unique prime factorization in group
        for f in U:
            sum_f = sum([f[p] * p for p in range(len(P))])
            for i in range(T, sum_f - 1, -1):
                dp[i] |= dp[i - sum_f]
    
    # Step 4: Return whether a subset sum of T exists in S
    return dp[T]


def prime_factorization(n):
    factors = Counter()
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 1:
        factors[n] += 1
    elif not factors:
        factors[n] += 1
    return factors
