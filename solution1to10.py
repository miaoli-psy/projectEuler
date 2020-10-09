# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:07:32 2020

@author: Miao
"""

# =============================================================================
# problem 1
# https://projecteuler.net/problem=1
# =============================================================================

res = 0
for num in range(1000):
    if num%3 == 0 or num%5 == 0:
        res += num
print(res)

# =============================================================================
# problem 2
# https://projecteuler.net/problem=2
# =============================================================================
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
def n_fibonacci(n):
    '''get the number n of fibonacci'''
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n_fibonacci(n-1) + n_fibonacci(n-2)

count = 1
n_fib = 1
while n_fib < 4000001:
    n_fib = n_fibonacci(count)
    count +=1

print("We need the %sth fibonacci"%(count-2)) #第32个覅波那切数符合条件


def sum_fobonacci(n):
    '''get the sum of the even_valued term'''
    sum_list = []
    for i in range(1, n+1):
        if n_fibonacci(i)%2 == 0:
            sum_list.append(n_fibonacci(i))
    return sum(sum_list), sum_list

sum_fobonacci(32)

# =============================================================================
# problem 3
# https://projecteuler.net/problem=3
# =============================================================================
a = 600851475143
prime = 0
for i in range(1,a-2):
    # test only odd number
    if i%2 != 0:
        i = i+2
        if a % i == 0:
            prime = i
            a = int(a/prime) #update a - run the for loop with new a-values
            break
    #skip even number
    else:
        continue
    print(i)





















