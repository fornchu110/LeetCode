#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
# By mod, time: O(1), space: O(1)
# ���wn, return n�M2���̤p������
# �]�N�O���u�nn�O���ƴN�^�Ǧۤv, n�O�_�ƴN�^��n*2
# �i�H�Q�Φ�B��ι�n%2���G�@�B�z�[�ֵ{���X�t��
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            # n<<1�N��n�����@bit, ���P���H2
            return n<<1
# @lc code=end

