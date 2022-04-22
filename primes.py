#This module returns primes factors (with multiplicity) of a number quickly.
#In addition, it can do several other operations including Euler totient funcion.
#run primes.about() to see the list of all functionality

#Written by Indrajit Jana. Suggestions are appreciated. Send those to ijana@iitbbs.ac.in
from math import sqrt

#Calculates the lowest prime factor by default
def factor(num:int)->int:
    '''
    

    Parameters
    ----------
    num : int
        Input number

    Returns
    -------
    int
       Lowest prime factor

    '''
    if num == 1:
        return 1
    if num==2 or num%2==0:
        return 2
    if num==3 or num%3==0:  # dakra added
        return 3            # dakra added
    else:
        for i in range(6, int(sqrt(num))+7, 6): # dakra Primes > 3 are all either
              if num%(i-1)==0: return i-1       # dakra 5 mod 6 or
              if num%(i+1)==0: return i+1       # dakra 1 mod 6
                                                # dakra saving all the tests for number which are 3 mod 6.
        else:
            return num

def check(num:int)->bool:
    '''
    

    Parameters
    ----------
    num : int
        Input number

    Returns
    -------
    bool
        True if the given number is prime

    '''
    if factor(num)==num:
        return True
    else:
        return False

def factors(num:int)->list:
    '''
    

    Parameters
    ----------
    num : int
        Given number

    Returns
    -------
    list
        List of prime factors

    '''
    fact=factor(num)
    new_num=num//fact
    factors=[fact]
    while new_num!=1:
        fact=factor(new_num)
        factors.append(fact)
        new_num//=fact
    return factors

def phi(num:int)->int:
    '''
    >>phi(9)
    6
    Because, these six numbers [1, 2, 3, 4, 5, 7] are mutually prime to 9

    Parameters
    ----------
    num : int
        Given number

    Returns
    -------
    int
        Number of integers less than the given number which are mutually prime to the given number
        

    '''
    val=num
    facts=factors(num) 
    sets=set(facts) 
    for i in sets:
        val=(val//i)*(i-1)
    return val
        

def __next_prime(given:list)->int: 
    if given==[2]:
        a=3
    else:
        a=given[-1]+2 #Next odd number (possible prime)
        found=False      
        while not found: 
            if a%6==3: a+=2      # dakra added. primes>3 are all either 1 or 5 mod 6. Skips 33% of candidates.
            imax=int(sqrt(a))+1  # dakra: will only test up to the sqrt(a) 
            for i in given:                
                if a%i==0:
                    a+=2   # dakra changed from +1 to +2 to skip testing even numbers
                    break  
                if i>=imax: # dakra no more testing required.
                    found=True
                    break
            
    return a


def first(n:int)->list:
    '''
    

    Parameters
    ----------
    n : int
        Integer input

    Returns
    -------
    list
        List of first n many primes

    '''
    given=[2]
    while len(given)<n:
        new_entry=__next_prime(given)
        given.append(new_entry)
    return given

def upto(n:int)->list:
    '''
    

    Parameters
    ----------
    n : int
        Integer input

    Returns
    -------
    list
        List of primes which are less than or equal to n.

    '''
    given=[2]
    while given[-1]<n: 
        new_entry=__next_prime(given)
        given.append(new_entry)
    if given[-1]>n:
        given=given[:-1] 
    return given

def between(m:int,n:int)->list:
    '''
    

    Parameters
    ----------
    m : int
        Lower bound.
    n : int
        Upper bound.

    Returns
    -------
    list
        List of primes in between m, and n (including m, n whenever applicable).

    '''
    x=[]
    d = 1 if m%2==0 else 0
    for i in range(m+d,n+1,2):
        if check(i):
            x.append(i)
    return x