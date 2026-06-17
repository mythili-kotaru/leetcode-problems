from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize map with None -> None. 
        # This brilliantly handles edge cases where curr.next or curr.random is None, 
        # and also handles the case where head is None right from the start!
        newMap = {None: None}
        
        curr = head
        # Pass 1: Clone all nodes and store them in the hash map
        while curr:
            newMap[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        # Pass 2: Assign next and random pointers using the map
        while curr:
            newNode = newMap[curr]
            newNode.next = newMap[curr.next]
            newNode.random = newMap[curr.random]
            curr = curr.next
            
        return newMap[head]

'''
Time Complexity: O(N)
- Where N is the number of nodes in the linked list.
- We iterate through the list exactly twice (once to create nodes, once to assign pointers). Thus, the runtime is strictly linear O(N).

Space Complexity: O(N)
- We use a hash map `newMap` to store mappings from original nodes to cloned nodes, which requires O(N) auxiliary space to hold all N nodes.
'''
