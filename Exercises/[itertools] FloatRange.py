# As you may know, the range function in Python allows coders to iterate over
# elements from start to stop with the given step. Unfortunately it works only
# for integer values, and additional libraries should be used if a programmer
# wants to use float values. Given float numbers start, stop and step, your task
# is to return a list of values from start to stop (including start and not
# including stop), evenly spaced by the step.

from itertools import count, takewhile


def solution(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)
