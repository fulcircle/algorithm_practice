#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_sets = {}
    pairs = 0

    for n in ar:
        if n in color_sets:
            color_sets[n] += 1
            if color_sets[n] % 2 == 0:
                pairs += 1
        else:
            color_sets[n] = 1

    return pairs

# print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()