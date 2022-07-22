# Given the list of the teams, your task is to come up with the list of all the
# games between them, and return them sorted lexicographically. for teams =
# ["Arsenal", "Chelsea", "Liverpool"] the result would be:
# [('Arsenal', 'Chelsea'), ('Arsenal', 'Liverpool'), ('Chelsea', 'Arsenal'),
# ('Chelsea', 'Liverpool'), ('Liverpool', 'Arsenal'), ('Liverpool', 'Chelsea')]

from itertools import permutations


def solution(teams):
    return sorted(permutations(teams, 2))