<<<<<<< HEAD
#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
# 倒a, bㄢ计, return a, bそ计计秖

# By simulation, time: O(min(a, b)), space: O(1)
# 纔て1: ざa, bぇ丁ぃ琌そ计, 璶min(a, b)计
# 眖1min(a, b)代刚a㎝b琌常俱埃, 碞琌%0, 讽Θミres+1
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        if a>b:
            tar = b
        else:
            tar = a
        for i in range(1, tar+1):
            if a%i==0 and b%i==0:
                res += 1
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
# 倒a, bㄢ计, return a, bそ计计秖

# By simulation, time: O(min(a, b)), space: O(1)
# 纔て1: ざa, bぇ丁ぃ琌そ计, 璶min(a, b)计
# 眖1min(a, b)代刚a㎝b琌常俱埃, 碞琌%0, 讽Θミres+1
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        if a>b:
            tar = b
        else:
            tar = a
        for i in range(1, tar+1):
            if a%i==0 and b%i==0:
                res += 1
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
