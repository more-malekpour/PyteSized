# Python's *itertools* Cheatsheet

- [Python's *itertools* Cheatsheet](#pythons-itertools-cheatsheet)
    - [Introduction](#introduction)
    - [Permutation, Combination, and Product](#permutation-combination-and-product)
    - [Repeat, Cycle, and Count](#repeat-cycle-and-count)
    - [Compress and Filterfalse](#compress-and-filterfalse)
    - [Dropwhile and Takewhile](#dropwhile-and-takewhile)
    - [Groupby](#groupby)
    - [Chain and Tee](#chain-and-tee)
    - [Accumulate](#accumulate)
    - [Miscellaneous](#miscellaneous)

### Introduction
There are multiple ways of creating iterator in Python. The easiest way is using built-in `iter` function. Another way is using comprehension with paranthesis instead of bracket. After converting a sequence to an iterator, functions such as `next` can be used.

```Python
>>> import itertools as it
>>> sequence = [1, 2, 3, 4]
>>> iterator_1 = iter(sequence)
>>> iterator_2 = (item for item in sequence)
```

### Permutation, Combination, and Product
The `permutations` are used when order/sequence of arrangement is needed, while the `combinations` are used to find the number of possible groups which can be formed.

```Python
>>> it.permutations(iterable, r=None)
# Returns r-length permutations of elements in the iterable.

>>> it.permutations('xyz', 3)
('x', 'y', 'z'), ('x', 'z', 'y'), ('y', 'x', 'z'),
('y', 'z', 'x'), ('z', 'x', 'y'), ('z', 'y', 'x')
```

```Python
>>> it.combinations(iterable, r)
# Creates all the unique combinations that have r members.

>>> it.combinations('xyz', 2)
('x', 'y'), ('x', 'z'), ('y', 'z')
```

The `combinations_with_replacement(iterable, r)` acts just like the `it.combinations()`, but allows individual elements to be repeated more than once:

```Python
>>> it.combinations_with_replacement('xyz', 2)
('x', 'x'), ('x', 'y'), ('x', 'z'), ('y', 'y'), ('y', 'z'), ('z', 'z')
```

In mathematics, **Cartesian Product** of two sets A and B is the set of all tuples of the form (a, b) where a is an element of A and b is an element of B. 

```Python
>>> it.product(*iterables, repeat=1)
# Creates the Cartesian product of iterables, equivalent to nested for-loops.

>>> it.product('xy', [1,2])
('x', 1), ('x', 2), ('y', 1), ('y', 2)
```

### Repeat, Cycle, and Count
These three functions return iterator objects whose `.__next__()` method generate consecutive values.

```Python
>>> it.repeat(object[, times])
# Repeats an object endlessly, unless there is a times argument.

>>> it.repeat('x', times=5)
'x', 'x', 'x', 'x', 'x'
```

```Python
>>> it.cycle(iterable)
# Cycles through an iterator over and over again.

>>> it.cycle('xyz')
'x', 'y', 'z', 'x', 'y', ...
```

```Python
>>> it.count(start=0, step=1)
# Returns evenly spaced values starting with number start.

>>> it.count(10, -0.5)
10, 9.5, 9.0, 8.5, 8.0, ...
```

### Compress and Filterfalse
While `compress` filters one iterable with another iterable, `filterfalse` only those elements for which the predicate function is **false**.

```Python
>>> it.compress(data, selectors)
# Filters one iterable with another.

>>> letters = ['w', 'x', 'y', 'z']
>>> selectors = [1, 0, 1, 0]
>>> it.compress(letters, selectors)
'w', 'y'
```

```Python
>>> it.filterfalse(predicate, iterable)
# Returns those elements for which predicate(item) is false.
# If predicate is not defined, returns the items that are false.

>>> sequence = [1, 2, 3, 4, 5, 6, 7, 1]
>>> result = it.filterfalse(lambda x: x < 4, sequence)
4, 5, 6, 7
```

### Dropwhile and Takewhile
The `dropwhile` makes an iterator that drops elements from the iterable as long as the predicate is true; afterwards, it returns every element. In contrast, the `takewhile` creates an iterator that returns elements from the iterable as long as the predicate is true; afterwards, it drop every element.

```Python
>>> it.dropwhile(predicate, iterable)
# Drops successive entries from an iterable as long as the predicate evaluates to true.

>>> sequence = [1, 2, 3, 4, 5, 6, 7, 1]
>>> result = it.dropwhile(lambda x: x < 4, sequence)
4, 5, 6, 7, 1
```

```Python
>>> it.takewhile(predicate, iterable)
# Returns successive entries from an iterable as long as the predicate evaluates to true.

>>> sequence = [1, 2, 3, 4, 5, 6, 7, 1]
>>> result = it.takewhile(lambda x: x < 4, sequence)
1, 2, 3
```

### Groupby
Unlike the convenient `groupby` function, the `it.groupby` returns grouped elements considering their adjacency. Therefore, if the universal grouping is desired, you must sort the elements first.

```Python
>>> it.takewhile(predicate, iterable)
# Returns successive entries from an iterable as long as the predicate evaluates to true.

>>> students = [{'name': 'David', 'age': 14},
>>>             {'name': 'Jesus', 'age': 18},
>>>             {'name': 'Aaron', 'age': 14},
>>>             {'name': 'Jacob', 'age': 18},
>>>             {'name': 'Marry', 'age': 18}]

>>> it.groupby(students, lambda x: x['age'])
Key 14: [{'name': 'David', 'age': 14}]
Key 18: [{'name': 'Jesus', 'age': 18}]
Key 14: [{'name': 'Aaron', 'age': 14}]
Key 18: [{'name': 'Jacob', 'age': 18}, {'name': 'Marry', 'age': 18}]

>>> students.sort(key=lambda x: x['age'])
>>> it.groupby(students, lambda x: x['age'])
Key 14: [{'name': 'David', 'age': 14}, {'name': 'Aaron', 'age': 14}]
Key 18: [{'name': 'Jesus', 'age': 18}, {'name': 'Jacob', 'age': 18},
         {'name': 'Marry', 'age': 18}]
```

### Chain and Tee 
The `chain` simply takes a number of iterables and returns them as one long iterable. However, the `tee` takes a single iterable and multiplicates it to **n** independent iterators.

```Python
>>> it.chain(*iterables)
# Chains multiple iterators together.

>>> it.chain('wx', 'yz')
'w', 'x', 'y', 'z'

>>> it.chain.from_iterable()
# Takes a single iterable of multiple iterables and chains them.

>>> it.chain.from_iterable(['wx', 'yz'])
'w', 'x', 'y', 'z'
```

```Python
>>> it.tee(iterable, n=2)
# Returns n independent iterators from a single iterable.

>>> letters = 'xyz'
>>> alpha_letters, beta_letters = it.tee(letters)
>>> alpha_letters
'x', 'y', 'z'
```

### Accumulate
The `accumulate` takes an iterable and a **binary** function (i.e., a function with precisely two inputs) and returns an iterator over accumulated results of applying the binary function to elements of the iterable.

```Python
>>> it.accumulate(iterable[, func])
# Makes an iterator that returns the results of a binary function.

>>> sequence = [1, 2, 3, 4, 5]
>>> it.accumulate(sequence, lambda x, y: x*y)
1, 2, 6, 24, 120
```

### Miscellaneous
The `starmap` function is similar to `*args` in terms of tuple unpacking.

```Python
>>> it.starmap(function, iterable)
# Computes the function using arguments obtained from the iterable.

>>> sequence = [(1, 2), (3, 4), (5, 6)]
>>> it.starmap(lambda x, y: x*y, sequence)
2, 12, 30
```

The `islice` works the same way as the standard slicing a list or tuple. However, it does not support extended slicing perfectly. For example, the step value should be a **positive** integer.

```Python
>>> it.islice(iterable, start, stop[, step])
# Cuts out a piece of an iterable, just like the standard slicing.

>>> sequence = [1, 2, 3, 4, 5]
>>> it.islice(sequence,0, 6, 2)
1, 3, 5
```

The `zip_logest` as its name implies, is an extension to the standard `zip` function, but iteration continues until the longest iterable is exhausted.

```Python
>>> it.zip_longest(*iterables, fillvalue=None)
# If the iterables are of uneven length, missing values are filled-in with fillvalue.

>>> numbers = [1, 2, 3, 4]
>>> letters = 'xyz'
>>> it.zip_longest(letters, numbers, fillvalue=None)
('x', 1), ('y', 2), ('z', 3), (None, 4)
```