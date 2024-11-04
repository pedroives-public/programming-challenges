"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3


Problem Source: LeetCode

Solution -> O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.result = None
        def inorder(node, k):
            if not node or self.counter >= k:
                return
            
            inorder(node.left, k)
            self.counter += 1
            if self.counter == k:
                self.result = node.val
                return

            inorder(node.right, k)
        
        inorder(root, k)
        return self.result