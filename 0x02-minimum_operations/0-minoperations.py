#!/usr/bin/python3
"Minimum Operations"


def minOperations(n):
    "operations"
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(int(n / i)) + i
