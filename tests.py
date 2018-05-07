#imports
import rsa
import prime_gen as pg
from primes_list import less_than_hundred_thousand

#imports#

#classes
#classes#

#functions
def testPrimesList():
    for i in less_than_hundred_thousand:
        assert(pg.rabin_miller_is_prime(i))
#functions#

#variables
#variales#

#main
#main#

def main():
    return 0

if __name__ == "__main__":
    main()
