#!/usr/bin/env python3


import sys
import time
import math


def binomial_coef(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def binomial(loops):
    base = loops / (3600 * 8)
    timer = time.time()
    overload = 0
    print("Binomial distribution:")
    for i in range(0, 51):
        res = binomial_coef(3500, i) * (base ** i) * ((1 - base) ** (3500 - i))
        if ((i + 1) % 5 != 0 and i < 50):
            print("%d -> %.3f" % (i, res), end='\t')
        else:
            print("%d -> %.3f" % (i, res))
        if i > 25:
            overload += res
    if loops > 320:
        overload = 1
    print("Overload: %.1f" % (overload * 100) + "%")
    end = time.time()
    print("Computation time: %.2f ms" % ((end - timer) * 1000))


def poisson(loop):
    base = 3500 * (loop / (60 * 60 * 8))
    timer = time.time()
    overload = 0
    print("\nPoisson distribution:")
    for i in range(0, 51):
        result = math.exp(-base) * (base ** i) / math.factorial(i)
        if (i + 1) % 5 != 0 and i < 50:
            print("%d -> %.3f" % (i, result), end='\t')
        else:
            print("%d -> %.3f" % (i, result), end='\n')
        if i > 25:
            overload += result
    if loop > 320:
        overload = 1
    print("Overload: %.1f" % (overload * 100) + "%")
    end = time.time()
    print("computation time: %.2f ms" % ((end - timer) * 1000))



def print_help():
    print("USAGE\n"
          "    ./203hotline [n k | d]\n\n"
          "DESCRIPTION\n"
          "    n      n value for the computation of C(n, k)\n"
          "    k      k value for the computation of C(n, k)\n"
          "    d      average duration of calls (in seconds)\n")


def main():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print_help()
    elif (len(sys.argv) == 2):
        try:
            num = int(sys.argv[1])
            binomial(num)
            poisson(num)
        except ValueError:
            sys.exit(84)
    elif (len(sys.argv) == 3):
        try:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
            print("{0}-combinations of a set of size {1}:\n{2}".format(k, n, binomial_coef(n, k)))
        except ValueError:
            sys.exit(84)
    else:
        sys.exit(84)
    return 0
