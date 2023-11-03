<<<<<<< HEAD
#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
# ���@�ӤG���}�Cmat�M���k, �C�@�C�ھ�1���ƶq�M�w�j�z, �̫�nreturn�ek�p���C��index
# ��C1�ƶq�V�P����, index���p�̸��z
# 1�`�O�b0������

# By binary search and heap, time: O(mlogn+klogm), space: O(m), �䤤m�O��ơBn�O�C��, ��space�Oheap�b�ƧǹL�{������
# �o�D�]��1�`�b0������, �i�H�ΤG���d��Ӭ�1����m�o��1���ƶq, �Ӥ��O���X����mat
# �n�Nhash�ƧǪ��D�ةγ\�令���]tuple��heap��n? �]��heap�����ƧǦӬO�b�إ߮ɨM�w��m
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            # l, r, pos = 0, n-1, -1
            # while l <= r:
            #     mid = (l + r) // 2
            #     if mat[i][mid] == 0:
            #         r = mid - 1
            #     else:
            #         pos = mid
            #         l = mid + 1
            # ��bisect�F��W���ĪG, bisect_left�N��J��ۦP�����ɧ䥪�䪺 
            # bisect_left()���Ѽƭn�O�ƧǦn��list
            # �Nmat���C�@�C��[::-1]�����F��ѥk�V����1���ĪG
            # ��n-�o��index-1�~�O������ɪ�index
            pos = n-bisect_left(mat[i][::-1], 1)-1
            # 1���ӼƬO�̫�@��1�Ҧbindex+1
            # �N1���ƶq�M�C��index�]��tuple��Jpower(list)
            power.append((pos+1, i))
        # �Npower�o��list�ഫ��heap, �o��heap�Omin heap, �ҥH1�ƶq�̤p���|�Q��b�W��
        # �O��o�ӻy�k, ��collections.deque()����
        heapq.heapify(power)
        res = list()
        for i in range(k):
            # �Nk�ӦC��index pop�X��
            res.append(heapq.heappop(power)[1])
        return res

# By hash and sorted, time: O(n^2), space: O(logn)
# �����X�@��mat�إߦn�C�C1�ƶq��hash, �A�Nhash�ھ�value(�]�N�O1���ƶq)���ƦC
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         hash = {}
#         for i in range(len(mat)):
#             tmp = 0
#             for j in range(len(mat[0])):
#                 if mat[i][j]==1:
#                     tmp += 1
#             hash[i] = tmp
#         # ���I, dict�u���sorted���٦��@��list, �S��dict.sort
#         # ���٦�list��N�S��dict���\��, �ӬO�Nkey�Mvalue�]���@��tuple
#         # �Ĥ@�ӰѼƳ]�w�Nhash���Ҧ������@�ƦC, key�N�Ox[1]�]�N�Ovalue
#         sortedhash = sorted(hash.items(), key = lambda x:x[1])
#         print(sortedhash)
#         res = []
#         # �N�ei��hash��key�[�J����
#         for i in range(k):
#             # [0]�Okey, [1]�Ovalue
#             res.append(sortedhash[i][0])
#         return res
        
        
# @lc code=end

=======
#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
# ���@�ӤG���}�Cmat�M���k, �C�@�C�ھ�1���ƶq�M�w�j�z, �̫�nreturn�ek�p���C��index
# ��C1�ƶq�V�P����, index���p�̸��z
# 1�`�O�b0������

# By binary search and heap, time: O(mlogn+klogm), space: O(m), �䤤m�O��ơBn�O�C��, ��space�Oheap�b�ƧǹL�{������
# �o�D�]��1�`�b0������, �i�H�ΤG���d��Ӭ�1����m�o��1���ƶq, �Ӥ��O���X����mat
# �n�Nhash�ƧǪ��D�ةγ\�令���]tuple��heap��n? �]��heap�����ƧǦӬO�b�إ߮ɨM�w��m
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            # l, r, pos = 0, n-1, -1
            # while l <= r:
            #     mid = (l + r) // 2
            #     if mat[i][mid] == 0:
            #         r = mid - 1
            #     else:
            #         pos = mid
            #         l = mid + 1
            # ��bisect�F��W���ĪG, bisect_left�N��J��ۦP�����ɧ䥪�䪺 
            # bisect_left()���Ѽƭn�O�ƧǦn��list
            # �Nmat���C�@�C��[::-1]�����F��ѥk�V����1���ĪG
            # ��n-�o��index-1�~�O������ɪ�index
            pos = n-bisect_left(mat[i][::-1], 1)-1
            # 1���ӼƬO�̫�@��1�Ҧbindex+1
            # �N1���ƶq�M�C��index�]��tuple��Jpower(list)
            power.append((pos+1, i))
        # �Npower�o��list�ഫ��heap, �o��heap�Omin heap, �ҥH1�ƶq�̤p���|�Q��b�W��
        # �O��o�ӻy�k, ��collections.deque()����
        heapq.heapify(power)
        res = list()
        for i in range(k):
            # �Nk�ӦC��index pop�X��
            res.append(heapq.heappop(power)[1])
        return res

# By hash and sorted, time: O(n^2), space: O(logn)
# �����X�@��mat�إߦn�C�C1�ƶq��hash, �A�Nhash�ھ�value(�]�N�O1���ƶq)���ƦC
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         hash = {}
#         for i in range(len(mat)):
#             tmp = 0
#             for j in range(len(mat[0])):
#                 if mat[i][j]==1:
#                     tmp += 1
#             hash[i] = tmp
#         # ���I, dict�u���sorted���٦��@��list, �S��dict.sort
#         # ���٦�list��N�S��dict���\��, �ӬO�Nkey�Mvalue�]���@��tuple
#         # �Ĥ@�ӰѼƳ]�w�Nhash���Ҧ������@�ƦC, key�N�Ox[1]�]�N�Ovalue
#         sortedhash = sorted(hash.items(), key = lambda x:x[1])
#         print(sortedhash)
#         res = []
#         # �N�ei��hash��key�[�J����
#         for i in range(k):
#             # [0]�Okey, [1]�Ovalue
#             res.append(sortedhash[i][0])
#         return res
        
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
