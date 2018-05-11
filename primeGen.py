#imports
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decorators import logged
import random
import primesList
import itertools
from math import sqrt
#imports#

#variables
#variables#

#classes
#classes#

#functions
def generateRandomPrime(bits):
    """Generate random prime number with at most n bits."""
    getRandomT = lambda: random.getrandbits(bits) | 1 << bits | 1
    print("Generating random T")
    p = getRandomT()
    for i in itertools.count(1):
        print("Checking if %d is prime"%p)
        if primeChecker(p):
            return p
        else:
            if i % (bits * 2) == 0:
                print("Getting newrandom number since we got a even")
                p = getRandomT()
            else:
                print("Adding two to a odd number")
                p += 2  # Add 2 since we are only interested in odd numbers


def basicIsPrime(n,K=100):
    """Returns True if n is a prime, and False it is a composite
    by trying to divide it by two and all the odd numbers lesser
    than or equal to the value in the position K. Returns
    None if test is inconclusive."""
    if n % 2 == 0:
        return n == 2
    if n in primesList.lessThanHundredThousand:
            return True
    return None

def millerTest(value,possiblePrime,debug = 1):
        #pick a random number a such that it is contained in [2,n-2].
        #corner cases guarantee that n will be bigger than 4.
        if(debug): print("Finding a random value")
        randomVal = random.randint(2,possiblePrime-2) % (possiblePrime-4)
        #Perform fast modular exponentiation
        if(debug): print("Performing fast modular exponentiation")
        fastModExp = pow(randomVal,value,possiblePrime)
        if(debug): print("Done.")
        if(fastModExp==1 or fastModExp == possiblePrime-1):
            return True
        if(debug): print("iteration starts here")
        while(value!= possiblePrime-1):
            fastModExp = (fastModExp*fastModExp) % possiblePrime;
            value *= 2;
            if(fastModExp == 1): return False
            elif(fastModExp== possiblePrime-1): return True
        if(debug): print("Iteration")
        return False

def millerPossiblePrime(possiblePrime,k=20):
        if(possiblePrime<=1 or possiblePrime==4): return False
        elif(possiblePrime<=3): return True
        #Pick a value such that value*2**r == n-1
        #Since every prime except 2 is odd, any prime-1 is even, by default,
        #can be written as value*2**r
        value = possiblePrime-1
        while(value%2==0):
            value/=2
        for i in range(k):
            if(millerTest(int(value),possiblePrime)==False):
                return False
        return True

def primeChecker(prime,k=20,debug = 1):
    if(debug): print("Checking if it is in the list")
    basic = basicIsPrime(prime)
    if not basic is None:
        return(basic)
    if(debug): print("Checking if it is a prime with miller method.")
    return(millerPossiblePrime(prime,k))
#functions#
