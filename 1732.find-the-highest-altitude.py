#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
# ���@list gain�N���P����, ���]���H����0�X�o, ���̧ۨǨ��Xgain�����P�۹ﰪ��
# return���X�L�{���̰��I�Ҧb
# Ex: gain = [-5, 1, 5, 0, -7], 0 -> -5 -> -4 -> 1 -> 1 -> -6, �ҥH�̰��I�b1

# By for loop, time: O(n), space: O(1)
# ���Xgain�L�{��+�B��Y�i���D��U����, �b����ثe�̰�����res�ɧ�s
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp = 0
        res = 0
        for i in gain:
            tmp += i
            # �U�����Pres = max(tmp, res)
            if tmp>res:
                res = tmp
        return res

# @lc code=end

