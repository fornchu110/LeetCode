<<<<<<< HEAD
#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
# 倒皚nums, 璝numsず┮Τじ=0 return 0, 璽 return -1, タ return 1

# By for loop, time: O(n), space: O(1)
# 钡ǐ砐, 笿じ琌0碞return 0, 璝璽计Τ计璽, Τ案计タ
# ぃノ璸计杠, 暗猭琌璸sign1, 窱<0碞跑-sign, 程return sign琌氮
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # 魁Τ碭璽计
        cnt = 0
        for i in nums:
            if i<0:
                cnt += 1
            elif i==0:
                return 0
        if cnt&1:
            return -1
        else:
            return 1
            
        
# @lc code=end

=======
#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
# 倒皚nums, 璝numsず┮Τじ=0 return 0, 璽 return -1, タ return 1

# By for loop, time: O(n), space: O(1)
# 钡ǐ砐, 笿じ琌0碞return 0, 璝璽计Τ计璽, Τ案计タ
# ぃノ璸计杠, 暗猭琌璸sign1, 窱<0碞跑-sign, 程return sign琌氮
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # 魁Τ碭璽计
        cnt = 0
        for i in nums:
            if i<0:
                cnt += 1
            elif i==0:
                return 0
        if cnt&1:
            return -1
        else:
            return 1
            
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
