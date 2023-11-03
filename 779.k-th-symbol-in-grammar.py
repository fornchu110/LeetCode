#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start

# ��l�Ƶ��@��Ʀr01, �u�n�o�檺��i�Ӥ����O0, �U�@��N�������X�{01, �p�G�O1�U�@��N�������X�{10
# ��n�Mk, ��X��n���k��int����(index�q1�}�l)
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

