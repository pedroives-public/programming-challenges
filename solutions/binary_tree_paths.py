"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.


Example 1:

    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

Example 2:

    Input: root = [1]
    Output: ["1"]


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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, node, path, result):
        if not node:
            return

        if not node.left and not node.right:
            result.append(path + str(node.val))
            return
        
        path += str(node.val) + "->"
        self.dfs(node.left, path, result)
        self.dfs(node.right, path, result)