#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
# By XOR and <<, time: O(n), space: O(1)
# �Hstart���_�I, �D�C�����Pstart+2��XOR��n-1�������G
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1, n):
            # i<<1�N��i����1�줸, ���P��2*i
            # �`�N�첾�u���v�b+-*/�U��, >=, ==...�W��, �ҥH�n�A��
            res ^= start+(i<<1)
        return res
        
# @lc code=end

