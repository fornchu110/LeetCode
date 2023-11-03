<<<<<<< HEAD
#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
# 璶―тnumsず程ㄢ计-1縩

# By for and if-elif, time: O(n), space: O(1)
# ノif㎝elif穦ΘミよΑ暗莱
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in nums:
            if i>=a:
                b = a
                a = i
            elif i>=b:
                b = i
        return (a-1)*(b-1)
        
# @lc code=end

=======
#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
# 璶―тnumsず程ㄢ计-1縩

# By for and if-elif, time: O(n), space: O(1)
# ノif㎝elif穦ΘミよΑ暗莱
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in nums:
            if i>=a:
                b = a
                a = i
            elif i>=b:
                b = i
        return (a-1)*(b-1)
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
