# Principles of algorithmic design

## Algorithm design paradigms
There are three general broad approaches to algirthm design
1. Divide and conquer
2. Greedy algorithms
3. Dynamic programming 

Some algorithms that use the divide and conquer paradigm are...
* Binary search
* Merge sort
* Quick sort
* Karatsuba algorithm for fast multiplication
* Strassen's matrix multiplication
* Closest pair of points

Greedy algorithms are generally used for optimization problems

Some algorithms that use the greedy paradigm are...
* Kruskals minimum spanning tree
* Dijkstra's shortest path
* Knapsack probelm
* Prim's minimal spannign tre algorithm
* Travelling salesman problem

## Recursion and backtracking
There are two types of recursive cases at it's core
* Base case - Terminate the recursive callbacks
* Recursive case - Function calls itself and progress towards achieving the base criteria

#### Some of the key differences are...
* Recursion is generally slower than iteration
* Each recursive call requires memory space, iteration does not
* Iteration doesn't require a stack to be generated

## Backtracking
Backtracking is a form of recursion that is particularly useful for types
of problems that involve being given multiple options that need to be pruned 
if they don't give the result that we need
