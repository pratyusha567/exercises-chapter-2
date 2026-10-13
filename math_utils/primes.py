from math import sqrt


def isprime(n):
    prime = True
    i = 2
    if n == 1:
        prime = False
    while i <= sqrt(n):
        if n%i == 0:
            prime = False
        i += 1
    return prime
