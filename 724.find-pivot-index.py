#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
# ���@�}�Cnums, �n�D��X�}�C���b����`�M���P�k�b����`�M��index

# By enumerate, time: O(n), space: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = 0
        for i in nums[1:]:
            r += i
        # �]�i��Hindex0����, ���Ml����0, ��r��n�]�O0, ���������������t
        if r==0:
            return 0
        # �`�N���צp�����, enumerate�|�qindex0�}�l
        for idx, i in enumerate(nums[1:]):
            l += nums[idx]
            r -= nums[idx+1]
            if l==r:
                #�]idx�O�q0�}�l, �ӧڹ�ڦb���X��idx�O�q1�}�l
                return idx+1
        return -1
        
# @lc code=end

