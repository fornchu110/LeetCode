#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
# By pair, time: O(n), space: O(1)
# ���r��s, �ݥi�H�����X��R�ML�ƶq�ۦP���l�r��
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        # �������h��R
        cnt = 0
        # �q�Y�ݨ��, ��R+1��L-1, ��0�ɥN��R�ML�ƶq�ۦP
        for i in s:
            if i=='R':
                cnt += 1
            elif i=='L':
                cnt -= 1
            if cnt==0:
                res += 1
        return res

# @lc code=end

