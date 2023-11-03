#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
# 要求出最大積的子數列
# 注意積的子數列只要乘上>1的數且負數為偶數個, 那一定至少越乘越大
# 遇到0才需要重置

# By count negtive, time: O(n), space: O(n)
# 會稍微比DP還快一些
# 偶數個負數的話越乘越大, 奇數個負數的話, 每個負數左右兩邊子數列一定有偶數個負數
# 反轉的用意是因整個數列不算子數列, 因此最長子數列絕對是nums[:len(nums)]或nums[1:len(nums)-1]奇一
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # reversed(nums)可以將nums反轉並回傳疊代器, 要用list接收
        # 記住反轉還能用nums.reverse()不回傳, 以及nums[::-1]切片方式
        reverse_nums = list(reversed(nums))
        # 將反轉後的nums走訪range(1, len(nums))等同於原本nums[:len(nums)-1]
        # 可以這樣做是因為乘法順序相反不會影響結果
        # 下面用一個for迴圈同時走訪兩個list
        for i in range(1, len(nums)):
            # or的目的是為了當遇到nums[i-1]為0時, 改乘上1
            # 複習or運算在左項非0時直接左項, 左項為0時才看右項, and運算左項為0時直接左項, 左項非0才看右項
            # 避免nums[i-1]=0時讓nums[i]也變成0, 乘一等同從nums[i]重新開始
            # 注意技巧是用nums和reverse_nums存上了走訪到i時的相乘結果
            # 所以最後用max()等同於找每種相乘結果裡面最大值, 得出答案
            nums[i] *= nums[i-1] or 1
            reverse_nums[i] *= reverse_nums[i-1] or 1
        # +是將兩list的拼接成一個list, 不會做對應項相加
        # Ex: a = [1, 2], b = [3, 4], a+b = [1, 2, 3, 4]
        return max(nums+reverse_nums)

# By DP, time: O(n), space: O(1)
# DP同時考慮min和max的原因是, 當min只要再遇到一個負數就可能變成max
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums:
#             return 
#         res = nums[0]
#         pre_max = nums[0]
#         pre_min = nums[0]
#         # nums[1:]的寫法可以不用range也從index為1的位置走訪, 且num仍代表nums[index]
#         for num in nums[1:]:
#             cur_max = max(pre_max*num, pre_min*num, num)
#             cur_min = min(pre_max*num, pre_min*num, num)
#             res = max(res, cur_max)
#             pre_max = cur_max
#             pre_min = cur_min
#         return res

# @lc code=end

