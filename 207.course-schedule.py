#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
# ���@�}�Cpreerqiosities, ���}�C���C�Ӥ�������0�Ӥ����O�ؼ�, ��1�Ӥ����O�ؼЫe������, return�Ӧ��}�C���Y�ण��b���d���ת����p�����Ҧ��ؼ�
# ���N�z�Ѭ����V�Ϥ��O�_��cycle, �Q���C�@�ӥ������Y�N�O�@��edge, �̭��������N��ۤ��P�I
# �Ӥ@�Ӧ��V�L���ϴN�s��DAG, �Ωݾ�ƧǪk��P�_, ���BFS�MDFS����
# �ݾ�ƧǪk�N�O�ﳻ�I���Ƨ�, �ϱo�C��edge(u, v)��v�@�����ץX�{�e, �Ҧ��@��v���ת�u���w�g���X�{

from collections import deque
# By BFS, time: O(N+M), space: O(N+M), N�Onode�ƶq�BM�Oedge�ƶq
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

# By DFS, time: O(N+M), space: O(N+M), N�Onode�ƶq�BM�Oedge�ƶq
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

