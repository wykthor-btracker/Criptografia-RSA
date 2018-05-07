#imports
import rsa
import prime_gen as pg
from primes_list import less_than_hundred_thousand

#imports#

#classes
#classes#

#functions
def testPrimesGenerator():
    assert(pg.rabin_miller_is_prime(pg.generate_random_prime(1024)))

#functions#

#variables
#variales#

#main
#main#

def main():
    return 0

if __name__ == "__main__":
    main()
