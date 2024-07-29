"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:

    Input: head = [1], n = 1
    Output: []

Example 3:

    Input: head = [1,2], n = 1
    Output: [1]


Problem Source: LeetCode

Solution -> O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            size, node, curr = 0, head, head
            while curr:
                size += 1
                curr = curr.next
            
            path = size - n - 1
            if path < 0:
                return head.next
            
            for i in range(path):
                node = node.next
            
            if node.next:
                node.next = node.next.next
            
            return head