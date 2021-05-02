#!/bin/python3

import math
import os
import random
import re
import sys


POSSIBLE= "Possible"
IMPOSSIBLE="Impossible"

# Complete the organizingContainers function below.
def organizingContainers(container):
    countByType=[0]* len(container[0])
    countByContainer=[sum(x) for x in container]
    for Ci in container: 
        print ("Ci=", Ci)
        for j in range(len(Ci)):
            print(" j=",j)
            countByType[j]+=Ci[j]
    countByContainer.sort()
    countByType.sort()
    return POSSIBLE if countByContainer==countByType else IMPOSSIBLE
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
