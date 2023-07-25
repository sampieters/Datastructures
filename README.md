# TwoThreeFourTree

## Introduction
This project was made as part of the course gegevensabstractie en -structuren It includes a 2-3-4 tree for which the 
rules can be found in the following link (https://www.geeksforgeeks.org/2-3-4-tree/).

## Rules
A 2-3-4 tree is a self-balancing data structure used to store and organize keys (and optionally associated values) in 
a sorted manner. It is a variant of the B-tree, with the primary difference being that a 2-3-4 tree nodes can have two, 
three, or four children, and the tree maintains the following rules to maintain balance:

### Insertion:

1. Start at the root and find the appropriate leaf node where the new key should be inserted.
2. If the leaf node has fewer than three keys, insert the new key into the leaf node while maintaining the keys in sorted order.
3. If the leaf node already has three keys (full node):
   - Perform a node split, creating a new node and moving the middle key up to the parent node (or create a new root if the parent is null).
   - Distribute the two remaining keys and the new key among the three child nodes.

### Deletion:

1. If the key to be deleted is in a leaf node, simply remove it from the leaf node.
2. If the key to be deleted is in an internal node, replace it with the smallest key in the right subtree (or the largest key in the left subtree) and recursively delete the smallest (or largest) key from the appropriate subtree.
3. If the deletion leads to an underflow in an internal node (less than two keys):
   - If a neighboring sibling has more than two keys, perform a "borrow" operation by rotating keys from the sibling.
   - If both the node and its siblings have two keys, perform a "fusion" operation by merging the node and one of its siblings into a single node and redistributing keys.

### Retrieval:

1. Start at the root and compare the search key with the keys in the current node.
2. If the search key matches one of the keys in the node, the search is successful, and the associated value (if present) is retrieved.
3. If the search key is less than the smallest key in the node, move to the left child and repeat the process.
4. If the search key is greater than the largest key in the node:
   - If the node has two children, move to the right child and repeat the process.
   - If the node has three or four children, move to the rightmost child and repeat the process.

### Dot:
There is also a function to write a .dot file of the current 2-3-4 tree. 