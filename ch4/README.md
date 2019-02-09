# Lists and Pointer structures

### Beginning with an example
* Supports for pointers exist within your computers hardware, known as indirect addressing.

```python
s = set()
```

`s` is not necessarily a set, rather a pointer that points to the beginning address of a set


### Arrays
* Arrays store pieces of data sequentially, meaning that all pieces of memory are also stored sequentially.
* If there isn't enough sequential memory to allocate for an array, there will be problems
* Arrays are very fast due to the fact that all memory is sequential, meaning that no jumps around to different bits of memory have to be made

### Pointer strcutures
* Pointer structures don't require continuous memory allocations in order to operate
* Because of this, they can start off relatively small and then grow tremondously in size without the worry of not having enough continuous space.
* However, they require more space to store the pointers that point the structure to the next node

### Working with nodes
* A really basic node can hold data and a pointer to the next node
within the structure
* In python, we will use `data` to represent data and `next` to represent
the next node.

### Singly linked lists
* A singly linked list is simply just a list where the nodes point to the
only the next nodes
* We can actually compose a singly linked list just using the `Node` class
we created in `node.py`.
