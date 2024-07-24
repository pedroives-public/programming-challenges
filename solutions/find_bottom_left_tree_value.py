"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:

    Input: root = [2,1,3]
    Output: 1

Example 2:

    Input: root = [1,2,3,4,null,5,6,null,null,7]
    Output: 7


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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)

        first = root.val
        while dq:
            first = dq[0].val
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)
        
        return first