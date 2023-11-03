#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
# By int(max()), time: O(n), space: O(1)
# �ƹ�W�N�O�䵹�w��n���C��Ƥ��̤j����, �]���p��������0�Y�i
class Solution:
    def minPartitions(self, n: str) -> int:
        # max�binput�r���, �|��r�ꤤascii�X�̤j���r��
        # ����A��int()�N�r���ഫ�����
        return int(max(n))

# @lc code=end

