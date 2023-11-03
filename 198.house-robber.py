#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
# 給一陣列nums, 在不取nums內相鄰元素下, 得到取的最大值

# By DP, time: O(n), space: O(1)
# 其實dp[i]不用想成必拿, 想成有i個元素下的最佳解即可
# 這樣dp[1]就可能是拿nums[0]或nums[1], 而dp[3]不用從dp[0]+nums[3]以及dp[1]+nums[3]選, 因為dp[1]時就該考慮到了
# 因此可以注意到一個更直接的轉移方程, 只有規定不能取相鄰的, 那實際上dp[i]就是max(dp[i-2]+nums[i], dp[i-1])
# 且最佳解只跟前兩個解有關, 所以只需要用兩或三個變數做迭帶即可省下空間
# 最後return dp[len(nums)-1]也就是最新的second
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, size):
            tmp  = second
            second = max(first+nums[i], second)
            first = tmp
            # 兩變數寫法, 但c不能這樣同時做運算
            # first, second = second, max(first + nums[i], second)
        return second

# By DP, time: O(n), space: O(n)
# 自己寫的作法
# 這題要注意的就是如何完成DP轉移方程, 原本以為只要比較奇數index元素和以及偶數index元素和
# 但實際上有這種case, nums = [2, 0, 0, 2], 可以發現取nums[0]+nums[3] = 4才是最佳解
# 觀察出無論怎麼取, 最後兩個元素必定會有一個被選走, 不可能在都不選的情況有最佳解(nums[i]必>0)
# 因此注意到, 假設把dp[i]當作必取nums[i]時的最佳解, 那dp[i] = max(dp[i-3]+nums[i], dp[i-2]+nums[i])
# 最後max(dp[len-1], dp[len-2])就是答案
# 這個想法可行, 但速度比較慢空間也花比較多
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return nums[0]
#         elif len(nums)==2:
#             return max(nums[0], nums[1])
#         elif len(nums)==3:
#             return max((nums[0]+nums[2]), nums[1])
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         dp[1] = nums[1]
#         dp[2] = max(dp[0]+nums[2], dp[1])
#         for i in range(3, len(nums)):
#             dp[i] = max(dp[i-3]+nums[i], dp[i-2]+nums[i])
#         return max(dp[len(nums)-2], dp[len(nums)-1])
        
# @lc code=end

