<<<<<<< HEAD
#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
# 給一陣列nums, 找出最少次對元素+1使得裡面元素是嚴格遞增(strictly increasing)的

# By simulation, time: O(n), space: O(1)
# 要嚴格遞增, 所以只要後面的<=前面的, 就要補上差值+1, 也就是再做差值+1次
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 不能做排序
        res = 0
        # 不需要做while迴圈, 會超時
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                # 注意要先更新結果再更新nums元素, 不然就是存起來
                # 否則結果會用到更新過的nums元素
                res += nums[i-1]-nums[i]+1
                nums[i] += nums[i-1]-nums[i]+1
        return res
    
# @lc code=end

=======
#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
# 給一陣列nums, 找出最少次對元素+1使得裡面元素是嚴格遞增(strictly increasing)的

# By simulation, time: O(n), space: O(1)
# 要嚴格遞增, 所以只要後面的<=前面的, 就要補上差值+1, 也就是再做差值+1次
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 不能做排序
        res = 0
        # 不需要做while迴圈, 會超時
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                # 注意要先更新結果再更新nums元素, 不然就是存起來
                # 否則結果會用到更新過的nums元素
                res += nums[i-1]-nums[i]+1
                nums[i] += nums[i-1]-nums[i]+1
        return res
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
