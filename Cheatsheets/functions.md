# Python's *Built-in Functions* Cheatsheet

- [Python's *Built-in Functions* Cheatsheet](#pythons-built-in-functions-cheatsheet)
    - [Map](#map)
    - [Filter](#filter)
    - [Eval](#eval)
    - [Int](#int)

### Map
The `map` function returns a map object (an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc.).

```Python
>>> map(function, iterable1[, iterable2, iterable3, ...])
# Loops over the items of an input iterable (or iterables).

>>> sequence_a = [1, 2, 3, 4]
>>> sequence_b = [5, 6, 7, 8]
>>> map(lambda x, y: x*y, sequence_a, sequence_b)
5, 12, 21, 32
```

### Filter
Python's `filter` is a built-in function that allows you to process an iterable and extract those items that satisfy a given condition.

```Python
>>> filter(function, iterable)
# Returns an iterator that is already filtered.

>>> sequence = [1, 2, 3, 4, 5, 6]
>>> filter(lambda x: x < 4, sequence)
1, 2, 3
```

### Eval
The `eval` function parse the Python's expressions from a string. It it good to note that the `eval` function has some major security implications and should be avoided if possible.

```Python
>>> eval(expression, globals=None, locals=None)
# Runs python expression passed to it.

>>> x = 8
>>> eval("x * 8")
64
```

### Int
Python's `int` function converts an string object to an integer in decimal with a given base.

```Python
>>> int(string, base=10)
# Returns an integer value equivalent to provided string in the given base. 

>>> string = '110'
>>> int(string, 2)
6
>>> int(string, 5)
30
>>> int(string)
110
```


