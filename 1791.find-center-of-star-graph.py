#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start

# By math, time: O(1), space: O(1)
# �쥻�Q���X�{�̦h�������I, �����]�D�جO���P�ι�, �u�����ߤ~�|�X�{�⦸�H�W, ��L�I���u�|�X�{�@��
# �]�������edge��X�@�P���I�N�O����
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
        #     return edges[0][0]
        # else:
        #     return edges[0][1] 
        # �W�����q���@�檩
        return edges[0][0] if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1] else edges[0][1]


# By hash, time: O(n), space: O(n), n�O�I���ƶq
# # ���h����, �䤤���I, ���N�O��X�{�̦h�������@�I
# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         res = 0
#         max = 0
#         hash = dict()
#         for i in range(len(edges)):
#             for j in range(2):
#                 if edges[i][j] not in hash:
#                     hash[edges[i][j]] = 1
#                 else:
#                     hash[edges[i][j]] += 1
#         # ��hash.items()�ӦP�ɨ��Xhash��key�Mvalue
#         for i, j in hash.items():
#             # ����val�ȳ̤j��, �N��key�O�U��
#             if j>max:
#                 max = j
#                 res = i
#         return res
        
# @lc code=end

