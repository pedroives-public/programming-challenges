"""
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

Example 1:

    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: true
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)

Example 2:

    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: false
    Example 3:

    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: true


Problem Source: LeetCode

Solution -> O(log(max(tx, ty)))
"""

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if not (tx >= sx and ty >= sy):
            return False
        
        while tx >= sx and ty >= sy:
            if tx == sx:
                return (ty - sy) % sx == 0
            elif ty == sy:
                return (tx - sx) % sy == 0
            elif tx > ty:
                tx %= ty
            else:
                ty %= tx
        
        return False
    
    """
    Lets take a simple case where only the y part changes
    sx = 2, sy = 3, tx = 2, ty = 11

    The tree would look like
    2,3 -> 2,5 -> 2,7 -> 2,9 -> 2,11

    ty can be written as:
    ty = sy + n * sx (n = number of times we add sx, in this case its 4)
    ty - sy = n * sx
    (ty - sy) % sx = (n * sx) % sx
    (ty - sy) % sx = 0
    """