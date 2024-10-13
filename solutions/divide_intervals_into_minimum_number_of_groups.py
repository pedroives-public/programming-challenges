"""
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

Example 1:

    Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    Output: 3
    Explanation: We can divide the intervals into the following groups:
    - Group 1: [1, 5], [6, 8].
    - Group 2: [2, 3], [5, 10].
    - Group 3: [1, 10].
    It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

Example 2:

    Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
    Output: 1
    Explanation: None of the intervals overlap, so we can put all of them in one group.


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        ordered = sorted(intervals, key=lambda idx: idx[0])

        for interval in ordered:
            events.append((interval[0], "start"))
            events.append((interval[1], "end"))
        
        active, ans = 0, 0
        # ordenação baseada no primeiro elemento, caso sejam iguais, o segundo é baseado na ordenação lexicografica entre start e end
        events = sorted(events, key=lambda idx: (-idx[0], idx[1]), reverse=True)
        # reverse=True pois faço a ordenação de forma contraria para que consiga ordenar os numeros da forma desejada, assim reverto tudo para que funcione do jeito desejado.

        for event in events:
            if event[1] == "start":
                active += 1
                ans = max(ans, active)
            else:
                active -= 1

        return ans