"""
Challenge2: plusMinus Zero
=========================

Given an list of integers, calculate the ratios of its elements that are positive, negative, and zero. 

Example:
--------
Input:
  arr = [-4, 3, -9, 0, 4, 1]

output:

  0.500000
  0.333333
  0.166667


"""


import math
import os
import random
import re
import sys


def plusMinusZero(arr):
    # Write your code here
    size = len(arr)
    count_arr = [0, 0, 0]
    for num in arr:
        if num > 0:
            count_arr[0] += 1
        elif num < 0:
            count_arr[1] += 1
        else:
            count_arr [2] += 1
    
    for count in count_arr:
        print("{:.6f}".format(count/size))
   
   
if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinusZero(arr)
