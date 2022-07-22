# Second Order Recurrence Relations: Generate Fibonacci sequence (i.e.,
# 0,1,1,2,3,5,8,13,...).

# Without Itertools
def fibs():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# With Functools
import functools as ft


def fibs(fibo_length):
    return ft.reduce(
        lambda memory, _: memory + [memory[-1] + memory[-2]], range(fibo_length), [0, 1]
    )


# With Itertools: robust for any other recurrence relations, such as Pell
# numbers or Lucas numbers.
import itertools as it


def second_order(p, q, r, initial_values):
    """Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
    intermediate = it.accumulate(
        it.repeat(initial_values), lambda s, _: (s[1], p * s[1] + q * s[0] + r)
    )
    return map(lambda x: x[0], intermediate)


fibs = second_order(p=1, q=1, r=0, initial_values=(0, 1))
# [0, 1, 1, 2, 3, 5, 8, 13]

pell = second_order(p=2, q=1, r=0, initial_values=(0, 1))
# [0, 1, 2, 5, 12, 29]

lucas = second_order(p=1, q=1, r=0, initial_values=(2, 1))
# [2, 1, 3, 4, 7, 11]
