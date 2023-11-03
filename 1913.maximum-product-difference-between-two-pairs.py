<<<<<<< HEAD
#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
# ���@��nums, �n�D�θ̭��|��index���P������a, b, c, d�D�Xa*b-c*d���̤j��

# By greedy, time: O(n), space: O(1)
# �]�u�O��§�X�̤j2�өM�̤p��Ӥ���, �������X���ƧǤ]��o�X��
# ��python��@�W��sotred()�ٺC, �i��O��ƶq�Ӥ�
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        # ��l�Ƴ̤j���
        mx1, mx2 = max(nums[0], nums[1]), min(nums[0], nums[1])
        # ��l�Ƴ̤p���
        mn1, mn2 = min(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(2, n):
            tmp = nums[i]
            if tmp>mx1:
                mx1, mx2 = tmp, mx1
            elif tmp>mx2:
                mx2 = tmp
            if tmp<mn1:
                mn1, mn2 = tmp, mn1
            elif tmp<mn2:
                mn2 = tmp
        return (mx1*mx2)-(mn1*mn2)

# �o���D�س�²��N�O���ƧǹL, ��̤j�⤸���M�̤p�⤸��
# By sorted(), time: O(n*log(n)), space: O(n)
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         sort = sorted(nums)
#         n = len(sort)
#         res = sort[n-1]*sort[n-2]-sort[1]*sort[0]
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
# ���@��nums, �n�D�θ̭��|��index���P������a, b, c, d�D�Xa*b-c*d���̤j��

# By greedy, time: O(n), space: O(1)
# �]�u�O��§�X�̤j2�өM�̤p��Ӥ���, �������X���ƧǤ]��o�X��
# ��python��@�W��sotred()�ٺC, �i��O��ƶq�Ӥ�
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        # ��l�Ƴ̤j���
        mx1, mx2 = max(nums[0], nums[1]), min(nums[0], nums[1])
        # ��l�Ƴ̤p���
        mn1, mn2 = min(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(2, n):
            tmp = nums[i]
            if tmp>mx1:
                mx1, mx2 = tmp, mx1
            elif tmp>mx2:
                mx2 = tmp
            if tmp<mn1:
                mn1, mn2 = tmp, mn1
            elif tmp<mn2:
                mn2 = tmp
        return (mx1*mx2)-(mn1*mn2)

# �o���D�س�²��N�O���ƧǹL, ��̤j�⤸���M�̤p�⤸��
# By sorted(), time: O(n*log(n)), space: O(n)
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         sort = sorted(nums)
#         n = len(sort)
#         res = sort[n-1]*sort[n-2]-sort[1]*sort[0]
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
