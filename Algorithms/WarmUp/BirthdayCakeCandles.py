#You are in charge of the cake for a child's birthday. 
#You have decided the cake will have one candle for each year of their total age. 
#They will only be able to blow out the tallest of the candles. 
#Count how many candles are tallest.

import sys

def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

