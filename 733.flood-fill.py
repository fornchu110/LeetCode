#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
# 給一個二維陣列image, 起始index: sr、sc和color, 從image[sr][sc]開始, 將所有相鄰數值等同image[sr][sc]的元素都替換為color

# By BFS, time: O(nm), space: O(nm)
# 這種走訪二維陣列或島嶼類型題目可以用DFS和BFS走訪, 能避免重複並同時做判斷
# 但BFS較為直觀
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currColor = image[sr][sc]
        # 一開始就相同那直接不用做
        if currColor==color:
            return image
        n, m = len(image), len(image[0])
        # 起始的index加入deque, 加入deque後更改color值
        queue = collections.deque([(sr, sc)])
        image[sr][sc] = color
        while queue:
            # popleft做到queue效果, 先進先出
            (x, y) = queue.popleft()
            # 將目前要處理的座標之上下左右座標做處理
            # 上下左右四個方向
            for mx, my in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                # 合法的座標才做處理, 不能超過邊界且要和初始color相同
                if 0<=mx<n and 0<=my<m and image[mx][my] == currColor:
                    # 合法的加入deque並更改color
                    queue.append((mx, my))
                    image[mx][my] = color
        return image

# By DFS, time: O(nm), space: O(nm)
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         n, m = len(image), len(image[0])
#         # 初始也會被更改, 所以要記錄下來
#         currColor = image[sr][sc]
#         # 子函式DFS, 將
#         def dfs(x: int, y: int):
#             # 每次走到新的座標都要確認是否和初始顏色相同, 相同就更改color
#             if image[x][y]==currColor:
#                 image[x][y] = color
#                 # 對相鄰符合邊界的座標都做dfs檢查並更改
#                 for mx, my in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
#                     if 0<=mx<n and 0<=my<m and image[mx][my]==currColor:
#                         dfs(mx, my)
#         # 當初始不等同要求的color就開始做DFS, 否則不需要做
#         if currColor!=color:
#             dfs(sr, sc)
#         return image

# @lc code=end

