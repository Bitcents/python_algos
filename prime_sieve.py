# the function returns a boolean array
# the indexes with a True value represent prime numbers
# since everything is zero-indexed
# you need to add 1 to the index number to get te
# prime number
def prime_seive(limit):
    primes = [True]*limit
    # 1 is not a prime number after all
    primes[0] = False
    for i in range(1, len(primes)):
        if primes[i]:
            for j in range(i+i+1, len(primes), i+1):
                primes[j] = False
    return primes
    


