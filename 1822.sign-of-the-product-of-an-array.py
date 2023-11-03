#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
# 給一陣列nums, 若nums內所有元素相乘=0 return 0, 相乘為負 return -1, 相乘為正 return 1

# By for loop, time: O(n), space: O(1)
# 直接走訪, 遇到元素是0的就return 0, 若負數有奇數個代表為負, 有偶數個代表為正
# 不用計數的話, 做法是計sign為1, 碰到<0的就變-sign, 最後return sign即是答案
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # 紀錄有幾個負數
        cnt = 0
        for i in nums:
            if i<0:
                cnt += 1
            elif i==0:
                return 0
        if cnt&1:
            return -1
        else:
            return 1
            
        
# @lc code=end

