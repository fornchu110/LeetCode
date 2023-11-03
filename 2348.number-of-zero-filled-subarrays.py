<<<<<<< HEAD
#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
# 倒皚nums, return柑贺硈尿0皚计ヘ

# By DP, time: O(n), space: O(1)
# 皚计ヘ璶癘眔硂┷
# Ex: [0]Τ1皚, [0, 0]Τ3皚, [0, 0, 0]Τ6皚
# ┮穦祇瞷, 1 = 0+1, 3 = 1+2, 6 = 3+3, –Ω祇瞷穝0碞+0计秖碞琌穝糤皚计ヘ
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
# 倒皚nums, return柑贺硈尿0皚计ヘ

# By DP, time: O(n), space: O(1)
# 皚计ヘ璶癘眔硂┷
# Ex: [0]Τ1皚, [0, 0]Τ3皚, [0, 0, 0]Τ6皚
# ┮穦祇瞷, 1 = 0+1, 3 = 1+2, 6 = 3+3, –Ω祇瞷穝0碞+0计秖碞琌穝糤皚计ヘ
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
