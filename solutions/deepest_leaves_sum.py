"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:

    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

Example 2:

    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 19


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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        dq = deque()
        dq.append(root)

        while dq:
            ans = 0
            size = len(dq)

            for _ in range(size):
                node = dq.popleft()
                ans += node.val

                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)
                    
        return ans