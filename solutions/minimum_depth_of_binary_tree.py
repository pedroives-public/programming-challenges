"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest 
path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: 2

Example 2:

    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5


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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        dq = deque()
        dq.append(root)

        numbers = 0
        while dq:
            numbers += 1
            paths = len(dq)
            
            for path in range(paths):
                node = dq.popleft()
                if node.left == None and node.right == None:
                    return numbers
                
                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)