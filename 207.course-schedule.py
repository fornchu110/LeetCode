#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
# 給一陣列preerqiosities, 此陣列內每個元素的第0個元素是目標, 第1個元素是目標前的先修, return照此陣列關係能不能在不卡先修的狀況完成所有目標
# 其實就理解為有向圖內是否有cycle, 想成每一個先修關係就是一個edge, 裡面的元素代表著不同點
# 而一個有向無環圖就叫做DAG, 用拓樸排序法能判斷, 能用BFS和DFS完成
# 拓樸排序法就是對頂點做排序, 使得每條edge(u, v)的v作為先修出現前, 所有作為v先修的u都已經先出現

from collections import deque
# By BFS, time: O(N+M), space: O(N+M), N是node數量、M是edge數量
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses

# By DFS, time: O(N+M), space: O(N+M), N是node數量、M是edge數量
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         def dfs(i, adjacency, flags):
#             if flags[i] == -1: return True
#             if flags[i] == 1: return False
#             flags[i] = 1
#             for j in adjacency[i]:
#                 if not dfs(j, adjacency, flags): return False
#             flags[i] = -1
#             return True

#         adjacency = [[] for _ in range(numCourses)]
#         flags = [0 for _ in range(numCourses)]
#         for cur, pre in prerequisites:
#             adjacency[pre].append(cur)
#         for i in range(numCourses):
#             if not dfs(i, adjacency, flags): return False
#         return True


# @lc code=end

