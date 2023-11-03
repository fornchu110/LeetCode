#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
# 給陣列nums和目標target, 在nums內搜尋到target return index, 搜尋不到return -1

# By binary search, time: O(nlogn), space: O(1)
# 基本的二分搜尋法, 注意範圍是[下界, 上界)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # 因是[下界, 上界), 所以right要是上界+1, 而下界上界範圍就是nums的index
        right = len(nums)
        # 不可能left==right, 因為left==right時[left, right)這區間不存在
        while left<right:
            # python不會溢位, 但先扣能避免
            mid = (right-left)//2+left
            # 找到target回傳index
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid
            else:
                left = mid+1
        # 如果找左相近, 則return left
        return -1
        
# @lc code=end

