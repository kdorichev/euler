"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1

The test data are from https://www.hackerrank.com/contests/projecteuler/challenges/euler001

Input data:
First line: 1<=T<=10**5 -- number of tests
Line 2...T+1 -- N: 1<=N,+10**9

Example of input data:
2
10
100
    """
T = int(input())
for i in range(T):
    N = int(input())
    # 3*(1+2+...+N//3)
    N3 = N//3
    if N%3 == 0: N3 -=1 # exclude last index
    # 5*(1+2+...+N//5)
    N5 = N//5
    if N%5 == 0: N5 -=1 # exclude last index
    N15 = N//15         # to exclude elements counted twice
    if N%15 == 0: N15 -=1
    # Use Sum of Ariphmetic Progression
    summa = int(3*(1+N3)*N3//2 + 5*(1+N5)*N5//2 - 15*(1+N15)*N15//2)
    print(summa)
