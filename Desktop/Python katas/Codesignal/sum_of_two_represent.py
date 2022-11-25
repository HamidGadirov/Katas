# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

def solution(n, l, r):
    count = 0
    # # for a in range(l, r + 1):
    # #     for b in range(l, r + 1):
    # #         if a + b == n and b >= a:
    # #             count += 1

    for a in range(l, r + 1):
        if a <= n - a <= r:
            count += 1
    return count