# This tool returns successive r length permutations of elements in an iterable.
#
# If r is not specified or is None, then r defaults to the length of the iterable,
# and all possible full length permutations are generated.
#
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted,
# the permutation tuples will be produced in a sorted order.

# Sample Input
#
# HACK 2
# Sample Output
#
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

from itertools import permutations

get_permutations = lambda word, length: '\n'.join(
    [''.join(perm) for perm in list(permutations(sorted([c for c in word]), length))])

if __name__ == '__main__':
    # w, l = input().split()
    # print(get_permutations(w, int(l)))
    print(get_permutations('HACK', 2))
