#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
# ��n�ӿO�w�@�}�l�O����, ��1�����}�Ҧ�, ��2���C2������, �]�N�O����i���n����i���ƿO�w���}��, return n���ᦳ�h�ֿO�w�G��

# By math, time: O(1), space: O(1)
# �[��W�ߵo�{, ��i�ӿO�w�Q���������ƴN�O��]�ƭӼ�
# �ҥH�����ƭӦ]�ƪ��O�w�̫�|�t, ���_�ƭӦ]�ƪ��O�w�̫�|�G
# �]���]�ƨ�⦨��, Ex: 2�O8���]��, ��8/2 = 4�]�O8�Ӧ]��, �o�ح�], �i�H�o�{�u���@�ر��p�]�Ƥ�����
# ���N�O���������, Ex: 3�O9���]��, ��9/3 = 3�w�g��L�F
# �ҥH�u����i�O��������Ƥ~�|���_�ƭӦ]��, �]���ˬdn�ӿO�w��������ƪ��ƶq�N�O����
# n�H����������ƪ��ӼƴN�O�ڸ�n
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # +0.5�O���F�b�B�I�B��ɦV�U����, �o�D���[�]�|�L
        return int(sqrt(n+0.5))

# @lc code=end

