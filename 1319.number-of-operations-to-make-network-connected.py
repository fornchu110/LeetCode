#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
# By DFS, time: O(n+m), space: O(n+m), m = len(connections)
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        edges = collections.defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)
        
        seen = set()

        def dfs(u: int):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)
        
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        
        return res - 1

# @lc code=end

