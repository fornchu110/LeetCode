#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start

# By while loop, time: O(lon(n)), space: O(1)
# time是O(log(n))的原因, n是input而n的位數會有10為底的log(n+1)
# 也就是說O(log(n))就是n的位數數量, 若n不是指input而是位數的話time: O(n)
# 要將input的n每位數相乘, 再將每位數相加, 最後積-和
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum = 0
        while(n!=0):
            pro *= n%10
            sum += n%10
            n//=10
        return pro-sum

# @lc code=end

