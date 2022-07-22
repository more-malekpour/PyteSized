# Python's *functools* Cheatsheet

- [Python's *functools* Cheatsheet](#pythons-functools-cheatsheet)
    - [Introduction](#introduction)
    - [Reduce](#reduce)
    - [Partial](#partial)

### Introduction
There are multiple ways of creating iterator in Python. The easiest way is using built-in `iter` function. Another way is using comprehension with paranthesis instead of bracket. After converting a sequence to an iterator, functions such as `next` can be used.

```Python
>>> import functools as ft
```

### Reduce
The `reduce` function is used to apply **folding** or **reduction**. It is useful when applying a function to an iterable and reducing it to a single cumulative value.

```Python
>>> ft.reduce(function, iterable[, initializer])
# Reduces the iterable to single cumulative result.

>>> sequence = [1, 2, 3, 4, 5, 6]
>>> ft.reduce(lambda x, y: x + y, sequence)
21
```

Both `reduce` and `accumulate` functions can calculate the accumulation of sequence elements. While the `reduce` returns the final value, the `accumulate` also provides an iterator of the intermediate values.

```Python
>>> import itertools as it
>>> sequence = [1, 2, 3, 4, 5, 6]
>>> it.accumulate(sequence, lambda x, y: x + y)
1, 3, 6, 10, 15, 21
```

There is a tricky way of simulating `accumluate` function with `reduce` via using intermediate list object:

```Python
>>> sequence = [1, 2, 3, 4, 5, 6]
>>> ft.reduce(lambda memory, new: memory + [memory[-1] + new], sequence, [0])
[1, 3, 6, 10, 15, 21]
```

There are similar functions in the well-known **NumPy** library. Both `reduce` and `accumulate` are methods of the universal functions. Currently, there are more than 60 universal functions defined ([Available Functions](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs)).

```Python
>>> import numpy as np
>>> seq = [1, 2, 3, 4, 5, 6]
>>> np.add.reduce(seq)
21

>>> np.add.accumulate(seq)
[1, 3, 6, 10, 15, 21]
```

### Partial
Python's `partial` function fixes a certain number of arguments of a function and generate a new function with pre-filled values.

```Python
>>> ft.partial(func, *args, **keywords)
# Forwards calls to func with assigned arguments and keywords.

>>> def original_func(x, y):
>>>     return f"X={x} & Y={y}"

>>> partial_func_1 = ft.partial(original_func, 0)
>>> partial_func_1(10)
'X=0 & Y=10'

>>> partial_func_2 = ft.partial(original_func, y=0)
>>> partial_func_2(10)
'X=10 & Y=0'
```

