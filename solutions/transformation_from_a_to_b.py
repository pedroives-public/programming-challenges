"""
Vasily has a number a, which he wants to turn into a number b. For this purpose, he can do two types of operations:

multiply the current number by 2 (that is, replace the number x by 2·x);
append the digit 1 to the right of current number (that is, replace the number x by 10·x + 1).
You need to help Vasily to transform the number a into the number b using only the operations described above, or find that it is impossible.

Note that in this task you are not required to minimize the number of operations. It suffices to find any way to transform a into b.

Input

    The first line contains two positive integers a and b (1 ≤ a < b ≤ 109) — the number which Vasily has and the number he wants to have.

Output

    If there is no way to get b from a, print "NO" (without quotes).

    Otherwise print three lines. On the first line print "YES" (without quotes). The second line should contain single integer k — the length of the transformation sequence. On the third line print the sequence of transformations x1, x2, ..., xk, where:

    x1 should be equal to a,
    xk should be equal to b,
    xi should be obtained from xi - 1 using any of two described operations (1 < i ≤ k).
    If there are multiple answers, print any of them.


Problem Source: Codeforces

Solution -> O(N)
"""

from collections import defaultdict

a, b = map(int, input().split())
tree = defaultdict(list)

def createTree(node, goal):
    if node is None or node > goal:
        return None
    
    if node == goal:
        return node
    
    left = createTree(2 * node, goal)
    right = createTree(10 * node + 1, goal)
    
    if left is not None:
        tree[node].append(left)
    if right is not None:
        tree[node].append(right)
    
    return node

def dfs(start, end, path):
    if start == end:
        return path
    
    if start not in tree:
        return None
    
    for son in tree[start]:
        if son not in path:
            new_path = dfs(son, end, path + [son])
            if new_path:
                return new_path
    
    return None

createTree(a, b)
result = dfs(a, b, [a])
if result is not None:
    print("YES")
    print(len(result))
    print(*result)
else:
    print("NO")