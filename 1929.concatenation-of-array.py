#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
# By extend, time: O(n), space: O(1)
# �n������nums�h�@����inums
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ��for�j��append�|�W��, python��ϥ�extend�����W�[�@��list
        nums.extend(nums)
        return nums

# @lc code=end

