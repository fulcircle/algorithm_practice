#!/bin/python3

# https://www.hackerrank.com/challenges/crush/problem

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = []
    b = []
    query_length = 0
    for query in queries:
        a.append((query[0], query[2]))
        b.append((query[1], query[2]))
        query_length += 1

    a.sort(key=lambda x: x[0])
    b.sort(key=lambda x: x[0])

    max_sum = current_sum = i = j = 0
    for num in range(1, n+1):

        while i < query_length and a[i][0] <= num:
            if a[i][0] == num:
                current_sum += a[i][1]
            i += 1
        
        while j < query_length and b[j][0] <= num-1:
            if b[j][0] == num-1:
                current_sum -= b[j][1]
            j += 1

        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


