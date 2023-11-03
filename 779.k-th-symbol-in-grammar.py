#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start

# 初始化給一行數字01, 只要這行的第i個元素是0, 下一行就對應的出現01, 如果是1下一行就對應的出現10
# 給n和k, 找出第n行第k個int的值(index從1開始)
class Solution:
    def kthGrammar(self, n, k):
        res = True
        n = 2**(n-1)
        while n!=1:
            n //= 2
            if k > n:
                k -= n
                res = not res
        if res:
            return 0
        else:
            return 1
# @lc code=end

