#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theGreatXor function below.


def toBase2(x):
  res = []

  while x != 0:
    remainder = x & 1
    res.append(remainder)

    x >>= 1

  res.reverse()

  return res


def theGreatXor(x):
  arr = toBase2(x)
  # print(arr)
  ans = 0

  for i in range(len(arr)):
    if arr[i] == 0:
      ans += 2**(len(arr) - 1 - i)

  return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

  q = int(input())

  for q_itr in range(q):
    x = int(input())

    result = theGreatXor(x)

    print(result)
    # fptr.write(str(result) + '\n')

  # fptr.close()


def solve():
  n = int(input())

  arr = list(map(int, input().split()))

  powerOfTwo = 1

  for _ in range(31):
    subset = 2**31 - 1

    for k in arr:
      if k & powerOfTwo != 0:
        subset &= k

    if subset == powerOfTwo:
      print('YES')
      return

    powerOfTwo <<= 1

  print('NO')


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
