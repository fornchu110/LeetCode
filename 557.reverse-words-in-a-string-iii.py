#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
# By string processing, time: O(n), space = O(1), n = len(s)
# �n�N���w�h�ӳ�r���Ǥ��ܤU, �����r�����e
# �Q��reversed()�N�r�ꤺ�e����, �`�Nreversed()�^�ǭȬO�@��list
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        # �r��]�i�H����, reversed()��^�ȬOlist, .reverse()�h�u��Φblist���i�Φb�r��
        # split()����]�O�o�D�ëD�����q��������Y, �ӬO��r���Ǥ��ܥu����C�ӳ�r���e
        # �]��split()�N��r����list�����P������, �A�̧ǹ�o�Ǥ���������
        s = s.split()
        for i in s:
            # �g��i = "".join(i[::-1])�]�i�H, [::-1]�O�������
            i = "".join(reversed(i))
            res.append(i)
        return " ".join(res)
        
# @lc code=end

