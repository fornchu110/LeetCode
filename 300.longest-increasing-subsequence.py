#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
# 給一個nums數列, return最常遞增子數列的長度
# 遞增子數列不用是連續的元素, 只要順序沒改變即可

# By DP, time: O(n^2), space: O(n), n = len(nums)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 當nums為空時代表沒有數列, 因此直接return 0
        if not nums:
            return 0
        # dp[i]代表著"包含了nums[i]"的前i個元素時最佳解, 也就是看包含nums[i]的前i個nums元素之最長子數列長度
        # 前0個元素不用討論, 所以討論前1個元素...前n個元素共len(nums)個
        dp = [1]*len(nums)
        # 探討dp[i]時的最佳解
        for i in range(len(nums)):
            # 前i個元素代表第0個元素到第i-1個元素共i個
            for j in range(i):
                # 只有nums[i]比nums[j]還大的情況, 才能從dp[j]+1轉移過來
                # Ex: 假設dp[3]也就是前三個元素最長是2, dp[4]也就是前四個元素最長是3
                # 這時我探討dp[5], 發現nums[5]>nums[3], 也就代表dp[5]可以是2+1 = 3
                # 這時再繼續探討dp[5], 發現nums[5]<nums[4], 就代表dp[5]不可以是3+1 = 4, 最多就到3了 
                # ex: nums = [0, 2, 1, 5, 4], 最長就是[0, 2, 5]等等長度為3的子數列
                if nums[i]>nums[j]:
                    # 之前的dp[i]從何而來?不只是初始化的1
                    # 假設目前j = 3, 那dp[i]也可能在j = 0, 1, 2, 3時更新過
                    # 因此需要求max
                    # Ex : 假設i = 7且dp[4] = 2, 走到這代表nums[7]>nums[3](dp[4]是包含nums[3]前4個時的解)
                    # 所以dp[7]可以是3, 但若前四個數是[1, 4, 5, 2], 那麼dp[3] = 3
                    # 所以實際上dp[7]應該在j = 2時就更新成4了, 不希望變成更小的3 
                    # 也就是說當這輪的nums[j]比之前的nums[j]還小時會發生dp[j]+1比dp[i]還小的狀況
                    dp[i] = max(dp[i], dp[j]+1)
        # 為什麼是max(dp)?
        # 因為dp[i]必須包含nums[i], 所以若nums[i]不是最大的就不可能會是最佳解, 與前面在看nums[j]同理
        return max(dp)
        
# @lc code=end

