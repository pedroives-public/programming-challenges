"""
Given the root of a binary tree, imagine yourself standing on 
the right side of it, return the values of the nodes you can see 
ordered from top to bottom.

Example 1:

    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

Example 2:

    Input: root = [1,null,3]
    Output: [1,3]

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if root == None:
            return results

        dq = deque([root])

        while dq:
            results.append(dq[0].val)
            size = len(dq)
            for _ in range(size):
                node = dq.popleft()

                if node.right != None:
                    dq.append(node.right)
                if node.left != None:
                    dq.append(node.left)

        return results