from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to keep track of already cloned nodes
        nodeMap = {}

        def dfs(curr_node):
            # If we've already cloned this node, return the clone
            if curr_node in nodeMap:
                return nodeMap[curr_node]
            
            # Create a new node with the same value
            newNode = Node(curr_node.val)
            
            # Important: Add to map BEFORE iterating neighbors to avoid infinite loops
            nodeMap[curr_node] = newNode

            # Recursively clone all neighbors
            for nei in curr_node.neighbors:
                newNode.neighbors.append(dfs(nei))
                
            return newNode
            
        return dfs(node) if node else None

'''
Time Complexity: O(V + E)
- Where V is the number of vertices (nodes) and E is the number of edges in the graph.
- The depth-first search traverses each node exactly once (O(V)), and iterates over each node's neighbors exactly once (O(E)).

Space Complexity: O(V)
- The hash map `nodeMap` stores the clones for every visited node, requiring O(V) space.
- The call stack for the recursive depth-first search will use up to O(V) space in the worst case (if the graph is essentially a linked list).
'''
