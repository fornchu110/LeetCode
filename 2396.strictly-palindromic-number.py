#
# @lc app=leetcode id=2396 lang=python3
#
# [2396] Strictly Palindromic Number
#

# @lc code=start
# By math, time: O(1), space: O(1)
# �n�P�_���winput n�q2~n-2�i��O�_���O�j��
# ���������s, �`�Ninput�q4~10^5
# ��n>=5��, (n-2)�i��|�O12, Ex: 5��3�i��=12, 6��4�i��=12
# ��n=4��, �G�i�100�]�D�j��, �]������return False�Y������
# n = 1*(n-2)^1+2*(n-2)^0 = n-2+2
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
        
# @lc code=end

