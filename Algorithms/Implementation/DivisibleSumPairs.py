https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
from itertools import combinations

def divisibleSumPairs(n, k, ar):
    res = 0
    comb = list(combinations(ar, 2))
    
    for pair in comb:
        if sum(pair) % k == 0:
            res += 1
    
    return res
    
        

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
