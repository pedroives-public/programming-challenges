"""
Given the root of a binary tree, return the bottom-up level order 
traversal of its nodes' values. (i.e., from left to right, level by level 
from leaf to root).

Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]

Example 2:

    Input: root = [1]
    Output: [[1]]

Example 3:

    Input: root = []
    Output: []


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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if root == None:
            return results
        
        dq = deque()
        dq.append(root)

        while dq:
            nodes = []
            paths = len(dq)

            for path in range(paths):
                node = dq.popleft()
                nodes.append(node.val)

                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)
            
            results.append(nodes)
        
        return results[::-1]