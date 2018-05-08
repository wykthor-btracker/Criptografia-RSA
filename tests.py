#imports
import rsa
import prime_gen as pg
from primes_list import less_than_hundred_thousand
from random import randint
#imports#

#classes
#classes#

#functions
def gcd(a,b):#Mathematically proven to work, so doesn't require its own test?
    if(b == 0):
        return(a)
    else:
        return gcd(b,a%b)

def testPrimesGenerator():
    assert(pg.rabin_miller_is_prime(pg.generate_random_prime(1024)))

def testPrimeGeneratesIntengerOrLong():
    assert(type(pg.generate_random_prime(1024)) == long or type(pg.generate_random_prime(1024)== int))

def testExtendedGcd():
    a,b = randint(0,1024),randint(0,1024)
    x,y = rsa.extended_gcd(a,b)
    greaterCommonDivisor = gcd(a,b)
    result = x*a+y*b
    assert(result==greaterCommonDivisor)

#functions#

#variables
#variales#

#main
#main#

def main():
    return 0

if __name__ == "__main__":
    main()
