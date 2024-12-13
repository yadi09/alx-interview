#!/usr/bin/python3
"Prime numbers"


def primeNumbers(n):
    "Return"
    primeN = []
    filterd = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filterd[prime]):
            primeN.append(prime)
            for i in range(prime, n + 1, prime):
                filterd[i] = False
    return primeN


def isWinner(x, nums):
    "Determine"
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeN = primeNumbers(nums[i])
        if len(primeN) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
