#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
# ���@�Ʋ�height, �̭��������O���P���ת�lines, ��X�Hlines�����ү�]�򪺳̦h���q
# �`�N�o�D�S��DP��, �]���S�����ƪ��l���D, ���i�H�z�Ѭ�Greedy

# By double pointer, time: O(n), space: O(1)
# ���pointer���O���V�Y����lines, ��X���i�઺�̤j���q
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        # �]���u���@��lines�S��k�]��, �ҥH��r-l==0�ɴN�פ�
        while r-l!=0:
            # �o�N�Olines��������, �Q������e��
            len_of_lines = r-l
            # ���q�O�H���C��lines�M�w��, �@��N�������]�|���|�X��
            # ���q�N�O�C��lines*�e��
            if min(height[l], height[r])*len_of_lines > res:
                res = min(height[l], height[r])*len_of_lines
            # ���H�b��, �C����ܰ��׸��C��lines����
            # �����ܰ��׸��C��lines���ʬO���T��?
            # �]���b�e�ץu���Y�p�����p, �L�ץt�@���ܦh��, ���q�������b���C��lines�o��
            # Ex, 2�M4, �Z��10, ���q=20, ���Ѧp�G�Z���n��9�Ӳ��ʪ��O4, �N��4�ܦ�400, ���q���O18(2*9)
            # �u�����ʤF��p��lines�~��"�i��"�o��̤j��, ���Ѳ���2�ܦ�200, �o�ɤ��q���M������4, ���ܦ�36(4*9)
            if height[l]<height[r]:
                l += 1
            # ��lines�@�˰����ܲ��ʽֳ���, �ڿ�ܲ���r
            else:
                r -= 1
        return res
        
# @lc code=end

