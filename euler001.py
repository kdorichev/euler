"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1

The test data are from https://www.hackerrank.com/contests/projecteuler/challenges/euler001

Input data:
First line: 1<=T<=10**5 -- number of tests
Line 2...T+1 -- N

Example of input data:
2
10
100
    """
T = int(input())
for i in range(T):
    N = int(input())
    aset = set(range(3,N,3))
    aset.update(range(5,N,5))
    print(sum(aset))

