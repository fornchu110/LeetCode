<<<<<<< HEAD
#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start

# By DFS
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        vis, ans, tot, size = [False] * n, 0, 0, 0
        def dfs(x: int) -> None:
            nonlocal size
            vis[x] = True
            size += 1
            for y in g[x]:
                if not vis[y]:
                    dfs(y)
        for i in range(n):
            if not vis[i]:
                size = 0
                dfs(i)
                ans += size*tot
                tot += size
        return ans

# @lc code=end

=======
#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start

# By DFS
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        vis, ans, tot, size = [False] * n, 0, 0, 0
        def dfs(x: int) -> None:
            nonlocal size
            vis[x] = True
            size += 1
            for y in g[x]:
                if not vis[y]:
                    dfs(y)
        for i in range(n):
            if not vis[i]:
                size = 0
                dfs(i)
                ans += size*tot
                tot += size
        return ans

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
