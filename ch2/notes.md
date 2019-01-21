# Principles of algorithmic design

## Deques
    1. Fast inserts and pops from either side
    2. Not sliceable, but can be sliced using `itertools.islice(iterable, start, end)`
    3. maxlen property can be set upon instantion to restrict the length of the deque
    4. `deque.rotate(n)` allows you to rotate the deque by n elements where if n greater than 0
    shift it right, and if n less than 0 shift it left 
    5. adds `appendleft`, `popleft`, `extendleft` to do operations to the left

## ChainMap
    1. Relate dictionaries to one another by putting all dictionaries into one list
    2. You can index any key from all dictionaries by indexing through the chainmap
    3. You can also get a dictionary at i, by accessing the `maps` list attached to the chainmap
    4. the chainmap will prioritize the key that comes first if the dictionaries that compose 
    the chainmap have the same key
    5. You can use `new_child` to create a child chainmap with modified properties
    6. you can use `parents` to find the parents of a chainmap

## Counter
    1. There are three ways to initiliaze a counter, through a sequential object, a dictionary, or tuple
    2. the `update` method takes an iterable or dictionary to update the count of each item within the counter
    3. The `update` method will not override values within the counter, rather add the count to previously existing keys
    4. Counter objects return 0 for keys that aren't stored within
    5. `Counter.elements()` returns an iterator where counts below one are not included and order isnt guaranteed

