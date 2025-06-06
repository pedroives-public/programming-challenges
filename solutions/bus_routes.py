"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Example 1:

    Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
    Output: 2
    Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

    Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
    Output: -1


Problem Source: LeetCode

Solution -> O(n * k)
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        queue = deque()
        for route_index in range(len(routes)):
            for stop in routes[route_index]:
                graph[stop].add(route_index)
        
        visited = set()
        visited_routes = set()
        visited.add(source)
        queue.append([source, 0])

        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses
            
            for route in graph[stop]:
                if route not in visited_routes:
                    visited_routes.add(route)
                    for bus in routes[route]:
                        if bus not in visited:
                            visited.add(bus)
                            queue.append([bus, buses + 1])
            
        return -1