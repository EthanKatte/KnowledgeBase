import time
'''

Array Manipulation:
- Search
 - Linear search: sequentially checks each element of an array until a match is found or the end of the array is reached. Simple but slow for large arrays.
 - Binary search: efficiently finds the position of a target value in a sorted array by repeatedly dividing the search interval in half. Requires a sorted array and is much faster than linear search for large arrays.
 - Interpolation search: an extension of binary search that works well for uniformly distributed data, where the midpoint of the search interval is estimated based on the values of the endpoints.
 - Jump search: a modification of linear search that works well for large arrays by jumping ahead a fixed number of steps instead of checking each element sequentially.
 - Exponential search: another modification of binary search that works by first finding a range where the target value might be located, and then performing binary search within that range.
 - Ternary search: a divide-and-conquer algorithm that repeatedly divides the search interval into three parts, reducing the search space by a factor of 2/3 each time. Can be used on both sorted and unsorted arrays.
 - Fibonacci search: another modification of binary search that uses the Fibonacci sequence to determine the next position to check. Can be faster than binary search for certain types of data.

'''
class ReturnValue():
    time = None
    operations = None
    retVals = None



class array():

    def __init__(self, values):
        self.values = values

    #O(n) Time Complexity
    def linerSearch(self, target): 
        start = time.time()
        ret = ReturnValue()
        for element in self.values:
            ret.operations+=1
            if target == element:
                ret.retVals = target
                ret.time = time.time() - start
                return ret
            
    #O(log(n)) Time Complexity
    def binarySearch(self, target): 
        start = time.time()
        ret = ReturnValue()
        vals = self.values
        right = len(vals)-1
        left = 0

        while left <= right:
            mid = (left + right)//2
            if vals[mid] == target:
                end = time.time()
                ret.time = end-start
                ret.retVals = target
                return ret
            elif vals[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        

        end = time.time()
        ret.time = end-start
        ret.retVals = None
        return ret
        return
            









'''
- Sort
 - Bubble sort: repeatedly swaps adjacent elements if they are in the wrong order
 - Selection sort: selects the minimum value and places it at the beginning, then repeats with the rest of the unsorted array
 - Insertion sort: inserts each element into its correct position in a sorted sublist, gradually building up the sorted array
 - Merge sort: recursively divides the unsorted array into two halves, sorts each half, and merges them back together
 - Quick sort: selects a pivot element, partitions the array into elements less than and greater than the pivot, and recursively sorts each partition
 - Heap sort: builds a binary heap data structure and repeatedly extracts the maximum element from it to build a sorted array
 - Radix sort: sorts elements by digit, sorting first on the least significant digit and working up to the most significant digit.

Tree Manipulation:
- Search
 - Depth-first search (DFS): explores as far as possible along each branch before backtracking. Can be implemented using either a stack (iterative DFS) or recursion (recursive DFS).
 - Breadth-first search (BFS): explores all nodes at a given depth before moving on to the next level. Can be implemented using a queue.
 - Uniform-cost search (UCS): finds the lowest-cost path by exploring paths in increasing order of cost. Uses a priority queue to keep track of the nodes to be expanded.
 - A* search: combines UCS with a heuristic function that estimates the cost of the cheapest path from a node to the goal. Uses a priority queue that orders nodes by the sum of the cost to reach the node and the estimated cost to get to the goal.
 - Bidirectional search: simultaneously searches from the start node and the goal node, meeting in the middle. Can be more efficient than traditional searches in certain situations.
 - Iterative deepening depth-first search (IDDFS): performs a series of DFS searches with increasing maximum depths until the goal is found. Combines the completeness of BFS with the space efficiency of DFS.
 - Monte Carlo tree search (MCTS): a probabilistic search algorithm commonly used in games and simulations. Builds a tree of possible moves and outcomes by repeatedly selecting and simulating moves.

- Types
 - Binary search trees (BSTs): a type of binary tree where each node has at most two children, and the left child is smaller than the parent, and the right child is greater than the parent. This allows for efficient searching, insertion, and deletion of values in sorted order.
 - Balanced search trees: a type of binary search tree that ensures the tree remains balanced, preventing worst-case performance in the search, insertion, and deletion operations. Examples include AVL trees and Red-Black trees.
 - B-trees: a type of multi-level balanced tree where each node contains multiple keys and child pointers. B-trees are often used in databases and file systems to provide efficient disk access.
 - Heap trees: a binary tree where each parent node is greater than or equal to its children (max heap) or less than or equal to its children (min heap). Heaps can be used to implement priority queues and sorting algorithms such as heapsort.
 - Trie trees: a tree-like data structure used to store and retrieve associative data, such as strings or sequences. Each node represents a prefix of a word, and the edges represent the next character in the word.
 - Segment trees: a tree-like data structure used to efficiently answer range queries on an array, such as finding the sum, minimum, or maximum of a range of elements. Each node represents a range of the array, and the values at each node are computed from the values of its children.

 - Tri-node restructuring
 


- Linked Lists:
 - Singly linked list: a linked list where each node has a reference to the next node but not the previous node.
 - Doubly linked list: a linked list where each node has references to both the next node and the previous node, allowing for efficient traversal in both directions.
 - Circular linked list: a linked list where the last node points back to the first node, forming a loop.

- Queue:
 - FIFO (First-In, First-Out) queue: a data structure where the first element added is the first element to be removed.
 - Priority queue: a data structure where each element has a priority value and the element with the highest priority is removed first.

- Heap:
 - Max heap: a binary tree where each parent node is greater than or equal to its children, and the root node contains the maximum value. Can be used to efficiently retrieve the maximum element from a collection of elements.
 - Min heap: a binary tree where each parent node is less than or equal to its children, and the root node contains the minimum value. Can be used to efficiently retrieve the minimum element from a collection of elements.


- Sets: 
 - Hash set: a set implementation that uses a hash table to store elements. Insertion, deletion, and membership tests take O(1) time on average.
 - Balanced search tree set: a set implementation that uses a balanced binary search tree (e.g., AVL tree or Red-Black tree) to store elements. This guarantees logarithmic time for insertion, deletion, and membership tests in the worst case.
 - Bit set: a set implementation that uses a bit array to represent a set of integers. This data structure is useful when the set elements are a small range of non-negative integers, since bit manipulation operations are very fast.
 - Trie set: a set implementation that uses a trie data structure to store elements. This is useful when the elements are strings or sequences, since tries can efficiently search for prefixes or suffixes.

- Graph Manipulation:

- Search
 - Dijkstra's algorithm: finds the shortest path between a source node and all other nodes in a weighted graph. Uses a priority queue to keep track of the nodes to be expanded.
 - Bellman-Ford algorithm: finds the shortest path between a source node and all other nodes in a weighted graph, allowing for negative edge weights. Can detect negative cycles.
 - A* search: combines Dijkstra's algorithm with a heuristic function that estimates the cost of the cheapest path from a node to the goal. Uses a priority queue that orders nodes by the sum of the cost to reach the node and the estimated cost to get to the goal.
 - Floyd-Warshall algorithm: finds the shortest path between all pairs of nodes in a weighted graph. Uses dynamic programming to compute the shortest paths in a matrix.
 - Kruskal's algorithm: finds the minimum spanning tree of a weighted, connected graph. Builds the tree by iteratively adding edges with the lowest weight.
 - Prim's algorithm: finds the minimum spanning tree of a weighted, connected graph. Builds the tree by iteratively adding edges with the lowest weight connected to the existing tree.
 - Topological sort: orders the nodes in a directed acyclic graph (DAG) such that for every directed edge from node A to node B, A comes before B in the ordering.

- Types
 - Directed graph: a graph where the edges have a direction, indicating a one-way relationship between nodes.
 - Undirected graph: a graph where the edges do not have a direction, indicating a two-way relationship between nodes.
 - Weighted graph: a graph where the edges have a weight or cost associated with them, indicating the "distance" between nodes.
 - Bipartite graph: a graph where the nodes can be divided into two sets such that there are no edges between nodes in the same set.
 - Complete graph: a graph where every pair of nodes is connected by an edge.
 - Sparse graph: a graph where the number of edges is much smaller than the number of possible edges.
 - Dense graph: a graph where the number of edges is close to the number of possible edges.


Other:
- Bloom Filter

'''