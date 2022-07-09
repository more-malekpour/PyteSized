# Python's *itertools* Cheatsheet

### Permuation & Combination

While **Permutations** are used when order/sequence of arrangement is needed, **Combinations** are used to find the number of possible groups which can be formed.

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

### Product

