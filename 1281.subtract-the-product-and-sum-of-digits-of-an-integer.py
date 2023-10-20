#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start

# By while loop, time: O(lon(n)), space: O(1)
# time琌O(log(n)), n琌inputτn计穦Τ10┏log(n+1)
# 碞琌弧O(log(n))碞琌n计计秖, 璝nぃ琌inputτ琌计杠time: O(n)
# 璶盢inputn–计, 盢–计, 程縩-㎝
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

