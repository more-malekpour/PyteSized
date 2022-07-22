# Given a list of numbers, Billy should calculate the following value:
# (((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...). Implement a function that,
# given a list of numbers, will return the result of the operation Billy has to
# perform.
# For numbers = [1, 2, 3, 4, 5, 6], the output should be solution(numbers) = 71.
# Here's how the answer is obtained: ((1 + 2) * 3 + 4) * 5 + 6 = 71.

import functools as ft


def solution(numbers):
    return ft.reduce(
        lambda x, y: x + y[1] if y[0] % 2 else x * y[1], enumerate(numbers), 1
    )
