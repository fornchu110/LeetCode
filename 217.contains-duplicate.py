#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# By set, time: O(n), space: O(n)
# time: O(n)��]�O�Nnums���e�@�@��Jset�]�nO(n), �p�G���⪺�ܴNO(1)
# python��set�h�����Ƥ���, �P�_set���׬O�_��nums�@�˧Y�i���D�O�_������
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # �����ƭnTrue, �]�N�O��̪��פ��P�ɷ|True, �ҥH��!=
        return len(nums)!=len(set(nums))

# By hash table, time: O(n), space: O(n)
# �p�G����nums�������Ƥ����Nreturn True, �_�hFalse
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash = dict()
#         for i in nums:
#             if i not in hash:
#                 hash[i] = 1
#             else:
#                 return True
#         return False

# By sort, time: O(n*log(n)), space: O(log(n))
# ��n�Ӥ����n�ƧǩҥHtime�OO(n*log(n))
# ��sort()��ڤW�O�λ��j, �ҥHspace: O(log(n))�K�Osort()��O���Ŷ�������
# �Nnums���ƧǦn, �P�_�Ƨǫ᪺nums��⤸���O�_�۵�
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return True
#         return False
        
# @lc code=end

