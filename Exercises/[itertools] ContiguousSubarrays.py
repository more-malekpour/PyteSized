# Return all the possible combination of contiguous sub-arrays of this array.

import itertools as it


def solution(array):
    indices = list(range(len(array) + 1))
    for i, j in it.combinations(indices, 2):
        yield array[i:j]