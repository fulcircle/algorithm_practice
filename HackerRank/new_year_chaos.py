#!/bin/python3

# https://www.hackerrank.com/challenges/new-year-chaos/

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    length = len(q)
    num_bribes = {}
    total_bribes = 0
    while True:
        swapped = False

        for i in range(1, length):
            if q[i] < q[i-1]:
                if q[i-1] not in num_bribes:
                    num_bribes[q[i-1]] = 1
                else:
                    num_bribes[q[i-1]] += 1

                if num_bribes[q[i-1]] > 2:
                    print('Too chaotic')
                    return
                
                q[i], q[i-1] = q[i-1], q[i]
                total_bribes += 1
                swapped = True

        if not swapped:
            break
                
    print(total_bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)