"""
Given the root of a binary tree, return the zigzag level order 
traversal of its nodes' values. (i.e., from left to right, then right to 
left for the next level and alternate between).

Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if root == None:
            return results
        
        dq = deque()
        dq.append(root)

        numbers = 0
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
            
            if numbers % 2 == 0:
                results.append(nodes)
            else:
                results.append(nodes[::-1])
            
            numbers += 1
        
        return results