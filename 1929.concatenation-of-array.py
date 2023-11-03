<<<<<<< HEAD
#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
# By extend, time: O(n), space: O(1)
# 要直接把nums多一份放進nums
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 用for迴圈append會超時, python能使用extend直接增加一個list
        nums.extend(nums)
        return nums

# @lc code=end

=======
#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
# By extend, time: O(n), space: O(1)
# 要直接把nums多一份放進nums
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 用for迴圈append會超時, python能使用extend直接增加一個list
        nums.extend(nums)
        return nums

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
