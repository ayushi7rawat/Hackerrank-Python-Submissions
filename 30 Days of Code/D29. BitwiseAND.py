#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    def FindMaxAB(n, k):
        max_ab = 0
        for i in range(k - 2, n):
            for j in range(i + 1, n + 1):
                ab = i & j
                if ab == k - 1:
                    return ab
                if max_ab < ab < k:
                    max_ab = ab
        return max_ab


    for i in range(int(input().strip())):
        n, k = map(int, input().split())
        print(FindMaxAB(n, k))