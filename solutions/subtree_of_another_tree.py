"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of 
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this 
node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false


Problem Source: LeetCode

Solution -> O(m * n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSameTree(pNode, qNode):
            if not pNode and not qNode:
                return True
            
            if not pNode or not qNode:
                return False

            if pNode.val != qNode.val:
                return False
            
            return checkSameTree(pNode.left, qNode.left) and checkSameTree(pNode.right, qNode.right)
        
        def checkSubTree(pNode, root):
            if not pNode and not root:
                return True
            
            if not pNode or not root:
                return False
            
            if checkSameTree(pNode, root):
                return True

            return checkSubTree(pNode.left, root) or checkSubTree(pNode.right, root)
        
        return checkSubTree(root, subRoot)