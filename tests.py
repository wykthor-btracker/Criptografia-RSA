#imports
import rsa
import prime_gen as pg
from primes_list import less_than_hundred_thousand
from random import randint
from math import sqrt
#imports#

#classes
#classes#

#functions
def gcd(a,b):#Mathematically proven to work, so doesn't require its own test?
    if(b == 0):
        return(a)
    else:
        return gcd(b,a%b)

def testPrimeGeneratesIntengerOrLong():
    try:
        assert(type(pg.generate_random_prime(1024)) == long or type(pg.generate_random_prime(1024)== int))
    except:
        print("If this is python 3, long doesn't exist anymore.")
        assert(type(pg.generate_random_prime(1024)==int))

def testExtendedGcd():
    a,b = randint(0,1024),randint(0,1024)
    x,y = rsa.extended_gcd(a,b)
    greaterCommonDivisor = gcd(a,b)
    result = x*a+y*b
    assert(result==greaterCommonDivisor)

def testPrimeChecker():
    for i in range(500):
        val = randint(2,2048)
        a = pg.primeChecker(val)
        b = True
        for i in range(2,val):#Slow but certain prime checking method
            if(val%i==0):
                print(val,i)
                b = False
                break
        if a!=b:
            assert a==b,"inconclusive at %d"%val
#functions#

#variables
#variales#

#main
#main#

def main():
    return 0

if __name__ == "__main__":
    main()
