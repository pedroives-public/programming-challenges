"""
Given that two linked lists are sorted in increasing order, create a new linked list representing the intersection of the two linked lists. The new linked list should be made without changing the original lists.

Note: The elements of the linked list are not necessarily distinct.

Examples:

Input: LinkedList1 = 1->2->3->4->6, LinkedList2 = 2->4->6->8
Output: 2->4->6
Explanation: For the given two linked list, 2, 4 and 6 are the elements in the intersection.

Input: LinkedList1 = 10->20->40->50, LinkedList2 = 15->40
Output: 40
Explanation: For the given two linked list, 40 is the only element in the intersection.


Problem Source: GeeksForGeeks

Solution -> O(n + m) where n and m are the lengths of the two linked lists.
"""

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self, head1, head2):
        
        answer = Node(None)
        tail = answer
        
        current1 = head1
        current2 = head2
        
        while current1 and current2:
            if current1.data == current2.data:
                tail.next = Node(current1.data)
                tail = tail.next
                current1 = current1.next
                current2 = current2.next
            
            elif current1.data < current2.data:
                current1 = current1.next
            else:
                current2 = current2.next
            
        return answer.next