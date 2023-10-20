#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start

# By hash table, time: O(n), space: O(1)
# ����hash�Nnums���������X�{���ưO���U��
# �[��찲�p�X�{3��, ��������goodpair�Ƭ�1+2 = 3 = (3*2)/2
# �X�{4��, goodpair: 1+2+3 = 6 = (4*3)/2, �O���t�ƦC
# ���t�ƦC����: n*(n+1)/2
class Solution:
    # �t�d���t�ƦC, �p��Ӥ�����goodpair��
    def arithmeticSequence(self, n):
        return (n*(n-1))//2

    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        hash = dict()
        # �N�����X�{���ưO���bhash��
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # ���Xhash�Q�ε��t�ƦC��Xgoodpair����
        for i in hash:
            res += self.arithmeticSequence(hash[i])
        return res

# By for loop, time: O(n^2), space: O(1)
# �ɤO�j���, ��C�Ӥ����������M�}�C��goodpair����
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         res = 0
#         # �]�����u�|�����, �ҥH��range
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 # �`�N��range��i�Mj�u�Oindex���Onums������
#                 # ��nums[i]�Mnums[j]�ӽT�{�����O�_�۵�
#                 if nums[i]==nums[j]:
#                     res += 1
#         return res

# @lc code=end

