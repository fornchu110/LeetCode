#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start

# By & and >>, time: O(log(num)), space: O(1)
# time: O(log(num))的原因是每次運算都會將num減半, 相當於以2為底做log
# 給num, 算出num經過幾次運算後才會變成0
# 規則是當num為偶數時直接除以2, 但若是奇數時-1
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while(num!=0):
            # 當num&1非0, 代表num是奇數
            if num&1:
                num -= 1
            # num是偶數
            else:
                # 除2等同於右移一位元, 注意如果用num/=2, num會變float而非int
                num >>= 1
            res += 1
        return res
        
# @lc code=end

