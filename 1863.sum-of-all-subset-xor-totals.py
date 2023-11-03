#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
# 找出nums內所有可能的subset, 再將其分別對內部元素做XOR, 沒元素就0, 只有一個元素就該元素值

# By DFS, time: O(2^n), space: o(n)
# 用dfs來窮舉subset
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        def dfs(val, idx):
            nonlocal res
            # 終止條件
            if idx==n:
                res += val
                return
            dfs(val^nums[idx], idx+1)
            dfs(val, idx + 1)  
        dfs(0, 0)
        return res


# @lc code=end

