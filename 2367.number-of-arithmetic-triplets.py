#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
# By hash, time: O(n), space: O(n)
# ��diff�Mnums, ��nums�����X��(i, i+diff, i+diff)�s�b
# ��hash�Y�i, �o�إu�n��Ҧ�input��i��B�L�����ƪ��i�H������set()
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        hash = dict()
        for i in nums:
            if i not in hash:
                hash[i] = i
            if i-diff in hash and i-diff-diff in hash:
                res += 1
        return res 

# By three pointer, time: O(n), space: O(1)
# �]nums�w�g�Ƨ�, �ҥH�i�H��pointer��@�D�ص���i�Bj
# �Q�k�O���Xnums���Ҧ�����, ������x�pdiff�������Ҧbindex j, �A���x�p2*diff�������Ҧbindex i
# ����N�N���@��n�D���զX
# class Solution:
#     def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
#         # j�qindex 1�}�l�O�]���T����index���୫��, (i, j, x)�ܤ֭n�O(0, 1, 2)
#         res, i, j = 0, 0, 1
#         for x in nums:
#             # �H�ۨ��Xnums, j�|�W�[�קK�F���ƲզX
#             while nums[j]+diff<x:
#                 j += 1
#             # ��ɱ���B�z, 
#             if nums[j]+diff>x:
#                 continue
#             while nums[i]+diff*2<x:
#                 i += 1
#             if nums[i]+diff*2==x:
#                 res += 1
#         return res

# @lc code=end

