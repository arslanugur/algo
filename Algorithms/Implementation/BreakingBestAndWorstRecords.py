https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys

def breakingRecords(score):
    arr_max = [score[0]]
    arr_min = [score[0]]
    
    for el in score[1:]:
        if el < arr_min[-1]:
            arr_min.append(el)
        if el > arr_max[-1]:
            arr_max.append(el)
            
    return str(len(arr_max)-1), str(len(arr_min)-1)
        

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
