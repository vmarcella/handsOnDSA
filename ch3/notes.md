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

## Runtime analysis
* Time complexity is used for mesasuring key operations being performed by the algorithm (such as comparison operators)
* Space complexity is used for measuring space taken up by data structures utilized within the algorithm

## Merge Sorting
Merge sorting consists of three simple steps...
1. Recursively sort the left half of the input array
2. Recursively sort the right half of the input array
3. Merge two sorted sub arrays into one

## Types of Algorithm analysis
1. Big O notation - The tight upper bound of an algorithm
2. Omega notation - The tight lower bound of an algorithm
3. Theta notation - Determines if O(F(n)) == Omega(F(n))
4. Amortized analysis - Analyzing an entire algorithms overall worst case runtime
