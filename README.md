# primes
This module contains several useful functions to work with prime numbers. For example, extracting all the prime factors (with multiplicity) of a positive integer reasonably fast. Following the list of all functions and their running time.

## Getting started
Download the file primes.py and place it in he same directory where your python is installed. Or simply run the command `pip install primes` to install the pachage.

## Available methods
You may run `primes.about()` afer installtion. The following is a list of all included mehods.


`primes.check(n)` returns *True* if *n* is a prime number.<br />
`primes.factor(n)` returns the lowest prime factor of *n*. <br />
`primes.facors(n)` returns all the prime factors of *n* with multiplicity.<br />
`primes.first(n)` returns first *n* many primes. <br />
`primes.upto(n)` returns all the primes less than or equal to *n*. <br />
`primes.between(m,n)` returns all the primes between *m* and *n*. <br />
`primes.phi(n)` returns the Euler's *phi(n)* i.e., the number of integers less than *n* which have no common factor with *n*. <br />


## Demonstration

This program is tested on my personal laptop with the following configurations.

>Processor: Intel(R) Core(TM) i3-4030U CPU @ 1.90Ghz<br/>
>Installed memory(RAM): 6.00GB <br/>
>System type: 64 bit Operating System, x64-based processor<br/>
>Operating system: Windows 10

### Small numbers

```
>>> primes.check(56156149)
False
>>> primes.check(789012345678901)
True
```
```

>>> primes.factor(7568945625)
3
>>> primes.factor(5141)
53
```



