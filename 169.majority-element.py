#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# 給一陣列nums, return在陣列中佔超過一半數量的元素
# 這樣的元素又被稱為眾數(mode)
# "超過一半"代表若有n個元素, 那出現次數至少>n/2
# 題目假設必定存在這樣的元素於陣列中

# By sort, time: O(nlogn), space: O(logn)
# 因必定存在這樣的元素, 可以觀察到超過一半的元素在排序後必定會在中間
# 所以排序後return即可
# 這題也可以用hash和divide and conquer做
# Boyer-Moore算法可以做到time: O(n), space: O(1), 以後研究
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 內建的sort()速度很快
        nums.sort()
        # 注意是"超過一半", 所以是要往上取整
        # Ex: [1, 1, 1, 2], 4個元素至少佔3個才算超過一半
        # 若(len(nums)-1)//2會在偶數個元素時往下取整
        # 往上取整就是(len(nums)-1+2-1)//2 = len(nums)//2
        return nums[len(nums)//2]
        
# @lc code=end
