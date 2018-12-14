# in this universe, 2 and 3 are ALWAYS, ALWAYS PRIME
known_prime = [2,3]
# a function that will find if a number is prime
def is_prime(n):
    print n
    totol_known_prime = len(known_prime)
    for i in range(0, totol_known_prime):
        if (n % known_prime[i] == 0):
            # THIS IS DIVISIBLE BY A PRIME NUMBER.
            # IT CANNOT BE PRIME
            return False
        else:
            # its not divisible by this one.. But that doesn't mean 
            # its not prime. Its just not divisible by this number 
            continue
    # we went through All known primes, and never hit our return False...
    # which means, this wasn't divisible by any known prime,
    # so it must be prime append
    known_prime.append(n)
    return True
is_prime(6000)
print known_prime