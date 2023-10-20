#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
# By hash table, time: O(m+n), space: O(m), m�Ojewles����, n�Ostones����
# �n��jewels�����r�Ŧ@�bjewels���X�{�X��
# ���Njewels���e���X�@���[�Jhash table, �S�A���X�@��stone�ݦ���
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # set�bpython�Ohast table���@��, ���|�����Ƥ���
        # �i�H��add�Mremove, ����list��append�[�J
        jewelsSet = set(jewels)
        for i in stones:
            if i in jewelsSet:
                res += 1
        return res

# By for loop, time: O(m*n), space: O(1), m�Ojewles����, n�Ostones����
# �n��jewels�����r�Ŧ@�bjewels���X�{�X��
# �o�ؼg�k�C�����Xstones���e���^�hjewels���X�@�M, �ҥH�Om*n
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         res = 0
#         for i in stones:
#             if i in jewels:
#                 res += 1
#         return res

# @lc code=end

