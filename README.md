# primes
This module contains several useful functions to work with prime numbers. For example, extracting all the prime factors (with multiplicity) of a positive integer reasonably fast. Following the list of all functions and their running time.

## Getting started
Download the file primes.py and place it in he same directory where your python is installed. Or simply run the command 
```
>>>pip install primes
```
to install the package. After either of the above two methods you can call it by 
```
>>>import primes
```
 and then execute the available methods.

## Available methods
You may run `primes.about()` afer importing the package. The following is a list of all included methods.


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
All the following commands returnd results in less than *1 sec*.

```
>>> primes.check(56156149)
False
>>> primes.check(79012338765433)
True
```

```
>>> primes.factor(7568945625)
3
>>> primes.factor(5141)
53
```

```
>>> primes.factors(252)
[2, 2, 3, 3, 7]
>>> primes.factors(44410608)
[2, 2, 2, 2, 3, 3, 11, 23, 23, 53]
```

```
>>> primes.first(7)
[2, 3, 5, 7, 11, 13, 17]
>>> primes.first(37)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]
>>> primes.first(5000)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
. . . . 
. . . .
 48179, 48187, 48193, 48197, 48221, 48239, 48247, 48259, 48271, 48281, 48299, 48311, 48313, 48337, 48341, 48353, 48371, 48383, 48397, 48407, 48409, 48413, 48437, 48449, 48463, 48473, 48479, 48481, 48487, 48491, 48497, 48523, 48527, 48533, 48539, 48541, 48563, 48571, 48589, 48593, 48611]
```
Outcomes from the last command is truncated.

```
>>> primes.upto(16)
[2, 3, 5, 7, 11, 13]
>>> primes.upto(50000)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179
. . .
. . .
49789, 49801, 49807, 49811, 49823, 49831, 49843, 49853, 49871, 49877, 49891, 49919,
49921, 49927, 49937, 49939, 49943, 49957, 49991, 49993, 49999]
```

```
>>> primes.between(100,200)
[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> primes.between(100000,500000)
[100003, 100019, 100043, 100049, 100057, 100069, 100103, 100109, 100129, 100151, 100153,
100169, 100183, 100189, 100193, 100207, 100213, 100237, 100267, 100271, 100279, 100291

499661, 499663, 499669, 499673, 499679, 499687, 499691, 499693, 499711, 499717, 499729, 499739, 499747, 499781, 499787, 499801, 499819, 499853, 499879, 499883, 499897, 499903, 499927, 499943, 499957, 499969, 499973, 499979]
```

```
>>> primes.phi(128)
64
>>> primes.phi(561534567567457)
483618287856960
```
### A little bigger numbers

All the following commands returned results in less than *5 secs*.

```
>>> primes.factors(225213155169257839996967418467924041)
[599, 5743, 6949, 7673, 9073709, 135318058916441]
```

```
>>> primes.first(10000)[9999]
104729
```
The last command returns the 10000th prime.

## Suggestions
Feel free to drop your suggestion at the following email address<br/>
>Author: Indrajit Jana<br/>
>Email: ijana at temple dot edu



