from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(M + N) — we traverse both lists at most once,
        where M and N are the lengths of list1 and list2.
        Space Complexity: O(1) — we reuse existing nodes; only the dummy head is extra.
        """
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        # Attach the remaining nodes (at most one list will be non-empty)
        curr.next = list1 if list1 else list2

        return dummy.next
