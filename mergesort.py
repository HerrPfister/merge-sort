#!/usr/bin/env python

def mergesort(s):
    list_size = len(s)
    s1 = []
    s2 = []

    if list_size <= 1:
        return s

    for x in range(0, list_size/2):
        s1.append(s[x])

    for y in range(list_size/2, list_size):
        s2.append(s[y])

    s1 = mergesort(s1)
    s2 = mergesort(s2)

    return merge(s1,s2)


def merge(s1,s2):
    s = []
    while s1 and s2:
        if s1[0] <= s2[0]:
            s.append(s1.pop(0))
        else:
            s.append(s2.pop(0))

    while s1:
        s.append(s1.pop(0))
    while s2:
        s.append(s2.pop(0))

    return s

import sys, re

try:
    f = open(sys.argv[1], 'r')
    str_numbers = f.read()
    f.close
    if not re.search("^[0-9],.", str_numbers):
        str_numbers = str_numbers.replace(',', ' ')
        str_numbers = str_numbers.split()

        numbers = []
        for str_num in str_numbers:
            if "." in str_num:
                numbers.append(float(str_num))
            else:
                numbers.append(int(str_num))
    print mergesort(numbers)
except IOError:
    print ("File %s does not exist"%sys.argv[1])

