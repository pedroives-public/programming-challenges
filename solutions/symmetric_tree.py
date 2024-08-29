"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:

    Input: root = [1,2,2,null,3,null,3]
    Output: false


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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            
            if not leftNode or not rightNode:
                return False
         
            if leftNode.val != rightNode.val:
                return False
            
            return (check(leftNode.left, rightNode.right) and check(leftNode.right, rightNode.left))

        return check(root.left, root.right)