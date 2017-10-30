
from decorators import logged
import random
import itertools
import primes_list


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

@logged("%b %d %Y - %H:%M:%S")
def generate_random_prime(bits, primality_test):
    """Generate random prime number with n bits."""
    get_random_t = lambda: random.getrandbits(bits) | 1 << bits | 1
    p = get_random_t()
    for i in itertools.count(1):
        if primality_test(p):
            return p
        else:
            if i % (bits * 2) == 0:
                p = get_random_t()
            else:
                p += 2  # Add 2 since we are only interested in odd numbers


def basic_is_prime(n, K=-1):
    """Returns True if n is a prime, and False it is a composite
    by trying to divide it by two and first K odd primes. Returns
    None if test is inconclusive."""
    if n % 2 == 0:
        return n == 2
    for p in primes_list.less_than_hundred_thousand[:K]:
        if n % p == 0:
            return n == p
    return None

def power(x, m, n):
    """Calculate x^m modulo n using O(log(m)) operations."""
    a = 1
    while m > 0:
        if m % 2 == 1:
            a = (a * x) % n
        x = (x * x) % n
        m //= 2
    return a 


def rabin_miller_is_prime(n, k=20):
    """
    Test n for primality using Rabin-Miller algorithm, with k
    random witness attempts. False return means n is certainly a composite.
    True return value indicates n is *probably* a prime. False positive
    probability is reduced exponentially the larger k gets.
    """
    b = basic_is_prime(n, K=100)
    if b is not None:
        return b

    m = n - 1
    s = 0
    while m % 2 == 0:
        s += 1
        m //= 2
    liars = set()
    get_new_x = lambda: random.randint(2, n - 1)
    while len(liars) < k:
        x = get_new_x()
        while x in liars:
            x = get_new_x()
        xi = pow(x, m, n)
        witness = True
        if xi == 1 or xi == n - 1:
            witness = False
        else:
            for __ in range(s - 1):
                xi = (xi ** 2) % n
                if xi == 1:
                    return False
                elif xi == n - 1:
                    witness = False
                    break
            xi = (xi ** 2) % n
            if xi != 1:
                return False
        if witness:
            return False
        else:
            liars.add(x)
    return True

if __name__ == '__main__':

    for b in [2 ** i for i in range(3, 12)]:
        print ("Generating %d-bit prime: " % b)
        print (generate_random_prime(b, rabin_miller_is_prime))



