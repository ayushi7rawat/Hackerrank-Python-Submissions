#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        emailID = firstNameEmailID[1]
        if '@gmail' in emailID:
            names.append(firstNameEmailID[0])

    names.sort()
    for i in range(len(names)):
        print(names[i])
