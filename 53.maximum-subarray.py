#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# By dynamic programming, time: O(n), space: O(1)
# ��X�̤j�l�}�C�M
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = 0
        # �`�N�@�}�l�n���ӳ̤j�M, �קK�u���@�Ӥ����ɪ����p
        res = nums[0]
        # ������T���Q�k
        # �ݹL�h�M�P��U����i���Ӥj, �j�̷�s�M
        # �o��s�M��, ����s�M�P�̤j�M���Ӥj, �j�̷�̤j�M
        for i in nums:
            if tmp+i<i:
                tmp = i
            else:
                tmp = tmp+i
            if tmp>res:
                res = tmp
        # �ڦۤv�����k
        # �ݹL�h�M+��U�����O�_>0, �Y<0�N��n�ΤU��>0������s�M
        # for i in nums:
        #     if tmp+i<0:
        #         tmp = 0
        #         # ���I, �N��L�h�M+��U����<0, ��U�����]�i���̤j�M�٤j
        #         if i>res:
        #             res = i
        #         continue
        #     else:
        #         tmp += i
        #         # �L�h�M+��U����>0�N�~��+, �Y>�̤j�M�h�����̤j�M
        #         if tmp>res:
        #             res = tmp
        return res
        
# @lc code=end

