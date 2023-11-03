<<<<<<< HEAD
#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
# ���@�G���}�C, 1�N���0�N���a, return�ʳ��q���ƶq
# ��@��0(���a)�P��|�Ӥ������O1(��), �N�N��O�ʳ��q��

# By DFS, time: O(mn), space: O(mn)
# �o�ثʳ��q�����D�N�����Q��BFS�MDFS
# class Solution:
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         # DFS
#         res = 0
#         directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
#         height, width = len(grid), len(grid[0])
#         for i in range(height):
#             for j in range(width):
#                 if grid[i][j] == 0:
#                     grid[i][j] = 1
#                     stack = []
#                     stack.append((i, j))
#                     flag = False
#                     while stack:
#                         x, y = stack.pop()
#                         if x == 0 or x == height - 1 or y == 0 or y == width - 1:
#                             flag = True
#                         for a, b in directions:
#                             m, n = x + a, y + b
#                             if 0 <= m < height and 0 <=n < width and grid[m][n] == 0:
#                                 grid[m][n] = 1
#                                 stack.append((m, n))
#                     if not flag:
#                         res += 1
#         return res

# By BFS, time: O(mn), space: O(mn)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # BFS
        res = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        height, width = len(grid), len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    queue = collections.deque()
                    queue.append((i, j))
                    flag = False
                    while queue:
                        x, y = queue.popleft()
                        if x == 0 or x == height - 1 or y == 0 or y == width - 1:
                            flag = True
                        for a, b in directions:
                            m, n = x + a, y + b
                            if 0 <= m < height and 0 <=n < width and grid[m][n] == 0:
                                grid[m][n] = 1
                                queue.append((m, n))
                    if not flag:
                        res += 1
        return res
    
# @lc code=end

=======
#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
# ���@�G���}�C, 1�N���0�N���a, return�ʳ��q���ƶq
# ��@��0(���a)�P��|�Ӥ������O1(��), �N�N��O�ʳ��q��

# By DFS, time: O(mn), space: O(mn)
# �o�ثʳ��q�����D�N�����Q��BFS�MDFS
# class Solution:
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         # DFS
#         res = 0
#         directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
#         height, width = len(grid), len(grid[0])
#         for i in range(height):
#             for j in range(width):
#                 if grid[i][j] == 0:
#                     grid[i][j] = 1
#                     stack = []
#                     stack.append((i, j))
#                     flag = False
#                     while stack:
#                         x, y = stack.pop()
#                         if x == 0 or x == height - 1 or y == 0 or y == width - 1:
#                             flag = True
#                         for a, b in directions:
#                             m, n = x + a, y + b
#                             if 0 <= m < height and 0 <=n < width and grid[m][n] == 0:
#                                 grid[m][n] = 1
#                                 stack.append((m, n))
#                     if not flag:
#                         res += 1
#         return res

# By BFS, time: O(mn), space: O(mn)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # BFS
        res = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        height, width = len(grid), len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    queue = collections.deque()
                    queue.append((i, j))
                    flag = False
                    while queue:
                        x, y = queue.popleft()
                        if x == 0 or x == height - 1 or y == 0 or y == width - 1:
                            flag = True
                        for a, b in directions:
                            m, n = x + a, y + b
                            if 0 <= m < height and 0 <=n < width and grid[m][n] == 0:
                                grid[m][n] = 1
                                queue.append((m, n))
                    if not flag:
                        res += 1
        return res
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
