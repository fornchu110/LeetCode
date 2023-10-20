#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
# ���@�ӳQrotated�L�����ǼƦC, ��X�̤p��
# rotated�w�q��:�N�ƦC�Q����cycle, rotate�@���N�N�Ҧ���������@��
# �Ʊ��Hlog(n)����

# By binary search, time: O(log(n)), space: O(1)
# �n�D��log(n)�n�Q��G���j�M�k, �C���u��ثe�d�򪺥b��Ҧ�time�Olog(n)
# �q�ثe�d�򤤶��������M���ɩM�k�ɤ��, �N�i�H���D�ؼ�(�̤p����)�b���b���٬O�k�b��
class Solution:
    def findMin(self, nums: List[int]) -> int:   
        # �N��0�Ӥ����M�̫�Ӥ����@���d��index, �`�Nr���O�Hlen(nums)�@��index 
        l, r = 0, len(nums)-1
        # �D�ػ����|�����Ƥ���, �u�n���O�u�Ѥ@�Ӥ�����l���|<r
        # �o�O�d�򬰥����k�}���g�k, �]�N�O�b[l, r)�j�M����, �G���d�䪺�϶��M�w�g�k, �O���H
        # l<r�N���Ҽ{l==r�����p�F, ����l==r�N��j�����϶��Ѥ@�Ӥ���, �Y�O����
        while(l<r):
            # pivot�O�ثe�d�򤤶�������
            # l+(r-l)//2���P��(l+r)//2, �O���F�קKl+r��overflow
            # ��ư��k�|��_right��a��left
            # Ex: 3�Ӥ���, l=0, r=2, mid = 1, array: 012
            # Ex: 4�Ӥ���, l=0, r=3, mid = 1, array: 0123
            pivot = l+(r-l)//2
            # pivot�p��r�N��̤p�Ȧb���b��
            if nums[pivot]<nums[r]:
                # �]�ڭ̤��Ʊ�j�M���ƪ��d��, �Ӳ{�b�O�����k�}, �ҥHr = pivot�U�����|�j�M�ثe��r
                r = pivot
            # �_�h�N��̤p�Ȧb�k�b��
            else:
                # �P�W, �����k�}�ҥHl+1�~���|�j�M�o����l
                l = pivot+1
        # �^��l��r���@��, �����N�Ol==r�ɵ����j�骺
        return nums[l]

# By min(), time: O(n), space: O(1) 
# python��min()�Mmax�N�u�O���X�@��, ��ڤW�S�٤U�ɶ�
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         return min(nums)
        
# @lc code=end

