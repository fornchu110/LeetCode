#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start

# By list, time: O(n), space: O(1) 
# space O(1)����]�Oreturn�����e����b�Ŷ�������
# �Ŷ������׳q�`��return�~�Ϊ��B�~�Ŷ�
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = list()
        # python�i�H������i�]list���e, �|���range��ٰO����
        # �o��i�N�N��nums[i]
        for i in nums:
            ans.append(nums[i])
        return ans

# By inplace replacement, time: O(n), space: O(1)
# �ɶ����Ŷ����@�k, ��a�ק�nums�����B�~�Ŷ�
# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         # 1000�O�]���D�ػ�nums���e���d��b[0, 999]
#         for i in range(n):
#             nums[i] += 1000*(nums[nums[i]]%1000) 
#         for i in range(n):
#             nums[i] //= 1000
#         return nums

# @lc code=end

