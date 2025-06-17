"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

Example 3:

    Input: root = [1,2,3,null,4], x = 2, y = 3
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dq = deque()
        dq.append([-1, root])
        
        while dq:
            parentX, parentY = -1, -1
            size = len(dq)
            for lvl in range(size):
                parent, node = dq.popleft()
                if node.val == x:
                    parentX = parent
                if node.val == y:
                    parentY = parent            

                if node.left:
                    dq.append([node.val, node.left])
                
                if node.right:
                    dq.append([node.val, node.right])
            
            if (parentX != parentY) and (parentX >= 0 and parentY >= 0):
                return True

        return False