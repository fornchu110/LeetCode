#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
# 給一陣列nums, 求在不取相鄰元素下得到最大和的取法, 同198題但差別在這個nums是個cycle
# 所以假設nums = [2, 0, 0, 2], 最大的取法是取nums[0]或nums[3] = 2, 不能取nums[0]+nums[3] = 4

# By DP, time: O(n), space: O(1)
# 其實核心想法和cycle一樣, 差別在於nums[0]和nums[len(nums)-1]只能取其中一個
# 也就是說, 計算dp[0:len(nums)-1]和dp[1:len(nums)]兩種情況, 找最大的那個即可
# 其實不用糾結在標記第一間房是否被偷, 這個做法把同時偷第一間和最後一間的可能性排除而已, 都有考慮只偷第一間, 或只偷最後一間, 或兩間都沒偷
# 把cycle拆成兩個序列的技巧要記得
class Solution:
    # 所以要找range在[0:len(nums)-1]時以及[1:len(nums)]時的最佳解做比較
    def rob(self, nums: List[int]) -> int:
        # 同198, 找最佳解, 只是給了範圍做計算
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start+2, end+1):
                first, second = second, max(first + nums[i], second)
            return second
        length = len(nums)
        if length==1:
            return nums[0]
        elif length==2:
            return max(nums[0], nums[1])
        else:
            # 兩種範圍的最佳解更大的那個就是答案
            return max(robRange(0, length-2), robRange(1, length-1))

        
# @lc code=end

