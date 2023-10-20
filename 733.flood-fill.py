#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
# ���@�ӤG���}�Cimage, �_�lindex: sr�Bsc�Mcolor, �qimage[sr][sc]�}�l, �N�Ҧ��۾F�ƭȵ��Pimage[sr][sc]��������������color

# By BFS, time: O(nm), space: O(nm)
# �o�ب��X�G���}�C�ήq�������D�إi�H��DFS�MBFS���X, ���קK���ƨæP�ɰ��P�_
# ��BFS�������[
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currColor = image[sr][sc]
        # �@�}�l�N�ۦP���������ΰ�
        if currColor==color:
            return image
        n, m = len(image), len(image[0])
        # �_�l��index�[�Jdeque, �[�Jdeque����color��
        queue = collections.deque([(sr, sc)])
        image[sr][sc] = color
        while queue:
            # popleft����queue�ĪG, ���i���X
            (x, y) = queue.popleft()
            # �N�ثe�n�B�z���y�Ф��W�U���k�y�а��B�z
            # �W�U���k�|�Ӥ�V
            for mx, my in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                # �X�k���y�Ф~���B�z, ����W�L��ɥB�n�M��lcolor�ۦP
                if 0<=mx<n and 0<=my<m and image[mx][my] == currColor:
                    # �X�k���[�Jdeque�ç��color
                    queue.append((mx, my))
                    image[mx][my] = color
        return image

# By DFS, time: O(nm), space: O(nm)
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         n, m = len(image), len(image[0])
#         # ��l�]�|�Q���, �ҥH�n�O���U��
#         currColor = image[sr][sc]
#         # �l�禡DFS, �N
#         def dfs(x: int, y: int):
#             # �C������s���y�г��n�T�{�O�_�M��l�C��ۦP, �ۦP�N���color
#             if image[x][y]==currColor:
#                 image[x][y] = color
#                 # ��۾F�ŦX��ɪ��y�г���dfs�ˬd�ç��
#                 for mx, my in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
#                     if 0<=mx<n and 0<=my<m and image[mx][my]==currColor:
#                         dfs(mx, my)
#         # ���l�����P�n�D��color�N�}�l��DFS, �_�h���ݭn��
#         if currColor!=color:
#             dfs(sr, sc)
#         return image

# @lc code=end

