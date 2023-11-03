#
# @lc app=leetcode id=2396 lang=python3
#
# [2396] Strictly Palindromic Number
#

# @lc code=start
# By math, time: O(1), space: O(1)
# 要判斷給定input n從2~n-2進制是否全是迴文
# 腦筋急轉彎, 注意input從4~10^5
# 當n>=5時, (n-2)進制都會是12, Ex: 5的3進制=12, 6的4進制=12
# 而n=4時, 二進制為100也非迴文, 因此直接return False即為答案
# n = 1*(n-2)^1+2*(n-2)^0 = n-2+2
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
        
# @lc code=end

